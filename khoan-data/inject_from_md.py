#!/usr/bin/env python3
"""
inject_from_md.py — Reads all .md files in khoan-data/, parses Điều/Khoản/Điểm,
and injects <details class="khoan"> into the HTML file.

Usage: python3 inject_from_md.py [--dry-run] [--doc DOC_ID]
"""
import re, html as html_mod, os, sys, argparse

HTML_PATH = os.path.join(os.path.dirname(__file__), '..', 'Mindmaps-on-thi-chuyen-doi-so-chi-tiet.html')
MD_DIR = os.path.dirname(__file__)

def parse_md(path):
    """Parse a .md file into {art_num: {title, khoans: [{num, text, diems}]}}"""
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    articles = {}
    current_art = None
    current_khoan = None
    pending_body = []  # plain-text lines before first numbered khoản

    def flush_body():
        if pending_body and current_art in articles and not articles[current_art]['khoans']:
            body = ' '.join(l.strip() for l in pending_body if l.strip())
            if body:
                articles[current_art]['khoans'].append({'num': 1, 'text': body, 'diems': []})
        pending_body.clear()

    for line in lines:
        stripped = line.rstrip()
        # Article header: ## Điều X. Title  OR  ## Mục X. Title
        art_m = re.match(r'^##\s+(?:Điều|Muc|Mục|Phần|Phan)\s+(\d+)[.\s]\s*(.*)', stripped)
        if art_m:
            flush_body()
            num = int(art_m.group(1))
            title = art_m.group(2).strip()
            current_art = num
            articles[num] = {'title': title, 'khoans': []}
            current_khoan = None
            pending_body.clear()
            continue
        if current_art is None or stripped.startswith('#') or stripped.startswith('<!--'):
            continue
        # Khoản: N. text (at line start, N = digit 1-30)
        khoan_m = re.match(r'^(\d+)\.\s+(.+)', stripped)
        if khoan_m:
            knum = int(khoan_m.group(1))
            ktext = khoan_m.group(2).strip()
            if 1 <= knum <= 30:
                flush_body()
                current_khoan = {'num': knum, 'text': ktext, 'diems': []}
                articles[current_art]['khoans'].append(current_khoan)
            continue
        # Điểm:    - x) text
        diem_m = re.match(r'^\s{2,}-\s+([a-zđ])\)\s+(.+)', stripped)
        if diem_m and current_khoan:
            current_khoan['diems'].append({'char': diem_m.group(1), 'text': diem_m.group(2).strip()})
            continue
        # Plain text body (article with no numbered khoản)
        if stripped:
            pending_body.append(stripped)

    flush_body()
    return articles

def make_khoan_html(art_data):
    lines = ['<div class="khoan-list">']
    for k in art_data['khoans']:
        preview = k['text'][:130] + ('…' if len(k['text']) > 130 else '')
        lines.append(f'<details class="khoan"><summary>'
                     f'<span class="khoan-num">Khoản {k["num"]}</span>'
                     f'<span class="khoan-text">{html_mod.escape(preview)}</span>'
                     f'</summary>')
        if k['diems']:
            lines.append('<div class="diem-list">')
            for d in k['diems']:
                lines.append(f'<div class="diem"><span class="diem-char">{d["char"]})</span>'
                             f'{html_mod.escape(d["text"][:200])}</div>')
            lines.append('</div>')
        lines.append('</details>')
    lines.append('</div>')
    return '\n'.join(lines)

def inject_card(content, doc_id, articles, dry_run=False):
    card_pat = re.compile(
        r'(<article[^>]+id="' + re.escape(doc_id) + r'"[^>]*>)(.*?)(</article>)',
        re.DOTALL)
    card_match = card_pat.search(content)
    if not card_match:
        print(f'  ⚠ Card {doc_id} not found in HTML')
        return content, 0
    card_content = card_match.group(2)
    injected = [0]
    skipped = [0]

    def replace_article(m):
        art_num_match = re.search(r'<span class="article-num"[^>]*>(?:Điều|Mục|Phần)\s*(\d+)', m.group(0))
        if not art_num_match:
            return m.group(0)
        art_num = int(art_num_match.group(1))
        if art_num not in articles or not articles[art_num]['khoans']:
            skipped[0] += 1
            return m.group(0)
        if 'khoan-list' in m.group(0):
            return m.group(0)  # already done
        khoan_html = make_khoan_html(articles[art_num])
        injected[0] += 1
        return re.sub(r'(</summary>)', r'\1\n' + khoan_html, m.group(0), count=1)

    new_card = re.sub(r'<details class="article"[^>]*>.*?</details>',
                      replace_article, card_content, flags=re.DOTALL)
    new_content = content[:card_match.start(2)] + new_card + content[card_match.end(2):]
    print(f'  {doc_id}: {injected[0]} injected, {skipped[0]} no-khoản')
    return new_content, injected[0]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--doc', help='Only inject specific doc ID')
    args = parser.parse_args()

    with open(HTML_PATH, 'r', encoding='utf-8') as f:
        content = f.read()

    total = 0
    md_files = sorted([f for f in os.listdir(MD_DIR) if f.endswith('.md') and not f.startswith('_')])
    for fname in md_files:
        doc_id = fname[:-3]  # strip .md
        if args.doc and doc_id != args.doc:
            continue
        md_path = os.path.join(MD_DIR, fname)
        if '<!-- TODO' in open(md_path).read():
            print(f'  ⏭ {doc_id}: TODO, skipping')
            continue
        articles = parse_md(md_path)
        total_k = sum(len(a['khoans']) for a in articles.values())
        if not articles:
            print(f'  ⚠ {doc_id}: no articles parsed from .md')
            continue
        print(f'  Parsing {doc_id}: {len(articles)} articles, {total_k} khoản')
        content, n = inject_card(content, doc_id, articles, args.dry_run)
        total += n

    if not args.dry_run:
        with open(HTML_PATH, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'\n✅ Done. Total {total} articles injected. File: {len(content):,} chars')
    else:
        print(f'\n[DRY RUN] Would inject {total} articles')

if __name__ == '__main__':
    main()
