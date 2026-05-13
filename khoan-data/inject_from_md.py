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
    """Parse a .md file into {art_num: {title, prefix, khoans: [{num, text, diems}]}}
    Also returns dominant_prefix (most common prefix used in ## headers)."""
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    articles = {}
    current_art = None
    current_khoan = None
    pending_body = []
    prefix_counts = {}

    def flush_body():
        if pending_body and current_art in articles and not articles[current_art]['khoans']:
            body = ' '.join(l.strip() for l in pending_body if l.strip())
            if body:
                articles[current_art]['khoans'].append({'num': 1, 'text': body, 'diems': []})
        pending_body.clear()

    roman = {'I':1,'II':2,'III':3,'IV':4,'V':5,'VI':6,'VII':7,'VIII':8,'IX':9,'X':10,
             'XI':11,'XII':12,'XIII':13,'XIV':14,'XV':15,'XVI':16,'XVII':17,'XVIII':18,'XIX':19,'XX':20}

    PREFIX_RE = re.compile(r'^##\s+(Điều|Muc|Mục|Phần|Phan)\s+(\d+|[IVX]+)[.\s]?\s*(.*)')

    for line in lines:
        stripped = line.rstrip()
        art_m = PREFIX_RE.match(stripped)
        if art_m:
            flush_body()
            prefix_raw = art_m.group(1)
            raw_num = art_m.group(2)
            num = roman.get(raw_num, None) if not raw_num.isdigit() else int(raw_num)
            if num is None:
                continue
            # Normalise prefix for HTML matching
            prefix = 'Điều' if prefix_raw in ('Điều',) else 'Mục' if prefix_raw in ('Muc', 'Mục') else 'Phần'
            prefix_counts[prefix] = prefix_counts.get(prefix, 0) + 1
            title = art_m.group(3).strip()
            current_art = num
            articles[num] = {'title': title, 'prefix': prefix, 'khoans': []}
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
    # Dominant prefix = most common one used in this .md
    dominant = max(prefix_counts, key=prefix_counts.get) if prefix_counts else 'Điều'
    return articles, dominant


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


def inject_card(content, doc_id, articles, dominant_prefix, dry_run=False):
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

    # Build a regex that matches ONLY the dominant prefix (to avoid cross-contamination)
    prefix_re = re.compile(
        r'<span class="article-num"[^>]*>(' + re.escape(dominant_prefix) + r')\s*(\d+)')

    def replace_article(m):
        art_match = prefix_re.search(m.group(0))
        if not art_match:
            return m.group(0)
        art_num = int(art_match.group(2))
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


def strip_wrong_injections(content, doc_id, keep_prefix):
    """Remove khoan-list from articles whose article-num does NOT match keep_prefix."""
    card_pat = re.compile(
        r'(<article[^>]+id="' + re.escape(doc_id) + r'"[^>]*>)(.*?)(</article>)',
        re.DOTALL)
    card_match = card_pat.search(content)
    if not card_match:
        return content, 0
    card_content = card_match.group(2)
    stripped = [0]

    def fix_article(m):
        art_text = m.group(0)
        if 'khoan-list' not in art_text:
            return art_text
        # Check if article-num prefix matches keep_prefix
        num_m = re.search(r'<span class="article-num"[^>]*>(.*?)</span>', art_text)
        if not num_m:
            return art_text
        label = num_m.group(1)
        if keep_prefix in label:
            return art_text  # correct injection, keep
        # Remove khoan-list div
        cleaned = re.sub(r'\n?<div class="khoan-list">.*?</div>\s*(?=</details>)', '', art_text, flags=re.DOTALL)
        if cleaned != art_text:
            stripped[0] += 1
        return cleaned

    new_card = re.sub(r'<details class="article"[^>]*>.*?</details>',
                      fix_article, card_content, flags=re.DOTALL)
    new_content = content[:card_match.start(2)] + new_card + content[card_match.end(2):]
    print(f'  {doc_id}: stripped {stripped[0]} wrong injections (kept prefix={keep_prefix})')
    return new_content, stripped[0]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--doc', help='Only inject specific doc ID')
    parser.add_argument('--cleanup', action='store_true', help='Strip wrong injections before re-injecting')
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
        articles, dominant = parse_md(md_path)
        total_k = sum(len(a['khoans']) for a in articles.values())
        if not articles:
            print(f'  ⚠ {doc_id}: no articles parsed from .md')
            continue
        print(f'  Parsing {doc_id}: {len(articles)} articles ({dominant}), {total_k} khoản')
        if args.cleanup:
            content, _ = strip_wrong_injections(content, doc_id, dominant)
        content, n = inject_card(content, doc_id, articles, dominant, args.dry_run)
        total += n

    if not args.dry_run:
        with open(HTML_PATH, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'\n✅ Done. Total {total} articles injected. File: {len(content):,} chars')
    else:
        print(f'\n[DRY RUN] Would inject {total} articles')

if __name__ == '__main__':
    main()
