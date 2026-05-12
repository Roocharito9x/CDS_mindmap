#!/usr/bin/env python3
"""Inject web-source blocks into Mindmaps-on-thi-chuyen-doi-so-v2-chi-tiet.html."""
from __future__ import annotations

import re
from html import escape

HTML_PATH = "/Users/ngochoang-ios/Downloads/BIDV AGENTIC 1.0/BMAD/docs/Tai lieu nang cao/Mindmaps-on-thi-chuyen-doi-so-v2-chi-tiet.html"

# card_id -> (status, [(label, url), ...], optional_note)
# status: web | partial (maps to data-status and badge class)
PATCHES: dict[str, tuple[str, list[tuple[str, str]], str | None]] = {
    "I.5": (
        "web",
        [
            ("Công báo — Luật 71/2025/QH15 (PDF)", "https://congbao.chinhphu.vn/tai-ve-van-ban-so-71-2025-qh15-45555-57751?format=pdf"),
            ("Thư viện pháp luật — toàn văn", "https://thuvienphapluat.vn/van-ban/Cong-nghe-thong-tin/Law-71-2025-QH15-Digital-Technology-Industry-668801.aspx"),
        ],
        None,
    ),
    "I.6": (
        "web",
        [
            ("Công báo — Luật 91/2025/QH15 (PDF)", "https://congbao.chinhphu.vn/tai-ve-van-ban-so-91-2025-qh15-45578-57730?format=pdf"),
            ("Bộ Công an — trang văn bản", "https://mps.gov.vn/chinh-sach-phap-luat/co-so-du-lieu-van-ban/luat-bao-ve-du-lieu-ca-nhan-1753688803"),
        ],
        None,
    ),
    "I.7": (
        "partial",
        [
            ("Phòng GD Cần Thơ — file đính kèm", "https://pbgdpl.cantho.gov.vn/attachment/6181"),
            ("VietISO — toàn văn (nguồn phụ)", "https://www.vietiso.com/blog/toan-van-luat-tri-tue-nhan-tao-2025-so-1342025qh15.html"),
        ],
        "Ưu tiên đối chiếu Công báo / Quốc hội khi có bản chính thức; URL hiện phục vụ đọc nhanh.",
    ),
    "I.8": (
        "web",
        [
            ("Văn bản QPPL — Luật Chuyển đổi số", "https://vanban.chinhphu.vn/?classid=1&docid=216335&orggroupid=1&pageid=27160"),
            ("Thư viện pháp luật — toàn văn", "https://thuvienphapluat.vn/van-ban/Cong-nghe-thong-tin/Luat-Chuyen-doi-so-2025-so-148-2025-QH15-675262.aspx"),
        ],
        None,
    ),
    "II.1": (
        "web",
        [
            ("Công báo — NĐ 53/2022/NĐ-CP", "https://congbao.chinhphu.vn/so-do-van-ban-so-53-2022-nd-cp-39253"),
            ("Thư viện pháp luật — toàn văn", "https://thuvienphapluat.vn/van-ban/Cong-nghe-thong-tin/Nghi-dinh-53-2022-ND-CP-huong-dan-Luat-An-ninh-mang-527750.aspx"),
        ],
        None,
    ),
    "II.2": (
        "web",
        [
            ("VBPL — Ngân hàng Nhà nước (toàn văn)", "https://vbpl.vn/nganhangnhanuoc/Pages/vbpq-toanvan.aspx?ItemID=177341"),
            ("Cổng Chính phủ — trang văn bản", "https://chinhphu.vn/?docid=213519&pageid=27160"),
        ],
        None,
    ),
    "II.3": (
        "web",
        [
            ("Công báo — tải DOC", "https://congbao.chinhphu.vn/tai-ve-van-ban-so-262-2025-nd-cp-46405-59380?format=doc"),
            ("Thư viện pháp luật — toàn văn", "https://thuvienphapluat.vn/van-ban/Cong-nghe-thong-tin/Nghi-dinh-262-2025-ND-CP-huong-dan-Luat-Khoa-hoc-Cong-nghe-va-doi-moi-sang-tao-677352.aspx"),
        ],
        None,
    ),
    "II.4": (
        "web",
        [
            ("Sở KHCN Đồng Nai — toàn văn", "https://skhcn.dongnai.gov.vn/vi/van-ban/detail/Nghi-dinh-so-265-2025-ND-CP-ngay-14-10-2025-cua-Chinh-phu-quy-dinh-chi-tiet-va-huong-dan-thi-hanh-mot-so-dieu-cua-Luat-Khoa-hoc-Cong-nghe-va-Doi-moi-sang-tao-ve-tai-chinh-va-dau-tu-trong-khoa-hoc-cong-nghe-va-doi-moi-sang-tao-37/"),
        ],
        "Nên đối chiếu thêm bản Công báo Chính phủ khi trích Điều.",
    ),
    "II.5": (
        "web",
        [
            ("Cổng Chính phủ — NĐ 356/2025/NĐ-CP", "https://chinhphu.vn/?docid=216387&pageid=27160"),
        ],
        None,
    ),
    "III.2": (
        "web",
        [
            ("Công báo — tải văn bản TT 15/2024", "https://congbao.chinhphu.vn/tai-ve-van-ban-so-15-2024-tt-nhnn-42185-50708"),
            ("Thư viện pháp luật — toàn văn", "https://thuvienphapluat.vn/van-ban/Tien-te-Ngan-hang/Thong-tu-15-2024-TT-NHNN-cung-ung-dich-vu-thanh-toan-khong-dung-tien-mat-615581.aspx"),
        ],
        None,
    ),
    "III.3": (
        "web",
        [
            ("Văn bản QPPL — TT 30/2025", "https://vanban.chinhphu.vn/?docid=215526&pageid=27160"),
            ("LuatVietnam — toàn văn", "https://luatvietnam.vn/tai-chinh/thong-tu-30-2025-tt-nhnn-sua-doi-thong-tu-15-2024-ve-dich-vu-thanh-toan-khong-dung-tien-mat-413828-d1.html"),
        ],
        None,
    ),
    "III.4": (
        "web",
        [
            ("Công báo — TT 17/2024", "https://congbao.chinhphu.vn/van-ban/thong-tu-so-17-2024-tt-nhnn-42189/50715.htm"),
            ("Thư viện pháp luật — toàn văn", "https://thuvienphapluat.vn/van-ban/Tien-te-Ngan-hang/Thong-tu-17-2024-TT-NHNN-mo-tai-khoan-thanh-toan-tai-to-chuc-cung-ung-dich-vu-thanh-toan-615776.aspx"),
        ],
        None,
    ),
    "III.5": (
        "web",
        [
            ("Công báo — TT 25/2025", "https://congbao.chinhphu.vn/van-ban/thong-tu-so-25-2025-tt-nhnn-46158.htm"),
            ("Thư viện pháp luật — toàn văn", "https://thuvienphapluat.vn/van-ban/Tien-te-Ngan-hang/Thong-tu-25-2025-TT-NHNN-sua-doi-Thong-tu-17-2024-TT-NHNN-672167.aspx"),
        ],
        None,
    ),
    "III.6": (
        "web",
        [
            ("Công báo — TT 18/2024", "https://congbao.chinhphu.vn/van-ban/thong-tu-so-18-2024-tt-nhnn-42190.htm"),
            ("Thư viện pháp luật — toàn văn", "https://thuvienphapluat.vn/van-ban/Tien-te-Ngan-hang/Circular-18-2024-TT-NHNN-bank-card-operations-619274.aspx"),
        ],
        None,
    ),
    "III.7": (
        "web",
        [
            ("Công báo — tải TT 50/2024", "https://congbao.chinhphu.vn/tai-ve-van-ban-so-50-2024-tt-nhnn-43225-52827"),
            ("Thư viện pháp luật — bài hỗ trợ / tra cứu", "https://thuvienphapluat.vn/phap-luat/ho-tro-phap-luat/thong-tu-502024-quy-dinh-ve-an-toan-bao-mat-cho-viec-cung-cap-dich-vu-truc-tuyen-trong-nganh-ngan-h-186349.html"),
        ],
        "Ưu tiên đọc file PDF trên Công báo để trích đúng Điều khoản.",
    ),
    "III.8": (
        "web",
        [
            ("Văn bản QPPL — TT 77/2025", "https://vanban.chinhphu.vn/?docid=216580&pageid=27160"),
            ("Thư viện pháp luật — toàn văn", "https://thuvienphapluat.vn/van-ban/Tien-te-Ngan-hang/Thong-tu-77-2025-TT-NHNN-sua-doi-Thong-tu-50-2024-TT-NHNN-688630.aspx"),
        ],
        None,
    ),
    "III.9": (
        "web",
        [
            ("Công báo — TT 64/2024 (PDF)", "https://congbao.chinhphu.vn/tai-ve-van-ban-so-64-2024-tt-nhnn-44057-54671?format=pdf"),
            ("Văn bản QPPL — metadata", "https://vanban.chinhphu.vn/?classid=1&docid=212621&pageid=27160"),
        ],
        None,
    ),
    "IV.1": (
        "web",
        [
            ("Báo điện tử Chính phủ — toàn văn NQ 57-NQ/TW", "https://xaydungchinhsach.chinhphu.vn/toan-van-nghi-quyet-ve-dot-pha-phat-trien-khoa-hoc-cong-nghe-doi-moi-sang-tao-va-chuyen-doi-so-quoc-gia-119241224180048642.htm"),
            ("Bộ Tư pháp — bản tin kèm link", "https://htpldn.moj.gov.vn/Pages/chi-tiet-tin.aspx?ItemID=642&l=Bantin"),
        ],
        None,
    ),
    "IV.2": (
        "web",
        [
            ("Công báo — NQ 71/NQ-CP (PDF)", "https://congbao.chinhphu.vn/tai-ve-van-ban-so-71-nq-cp-44701-55981?format=pdf"),
        ],
        None,
    ),
    "V.1": (
        "web",
        [
            ("Văn bản QPPL — QĐ 749/QĐ-TTg", "https://vanban.chinhphu.vn/?docid=200163&pageid=27160"),
            ("Hệ thống pháp luật — toàn văn", "https://hethongphapluat.com/quyet-dinh-749-qd-ttg-nam-2020-ve-phe-duyet-chuong-trinh-chuyen-doi-so-quoc-gia-den-nam-2025-dinh-huong-den-nam-2030-do-thu-tuong-chinh-phu-ban-hanh.html"),
        ],
        None,
    ),
    "V.2": (
        "web",
        [
            ("Báo Chính phủ — tin ban hành", "https://www.baochinhphu.vn/print/ban-hanh-quy-che-quan-ly-van-hanh-khai-thac-cong-dich-vu-cong-quoc-gia-102302140.htm"),
            ("LuatVietnam — toàn văn", "http://luatvietnam.vn/hanh-chinh/quyet-dinh-31-2021-qd-ttg-210949-d1.html"),
        ],
        None,
    ),
    "V.3": (
        "web",
        [
            ("Văn bản QPPL — QĐ 06/QĐ-TTg", "https://vanban.chinhphu.vn/?docid=205022&pageid=27160"),
            ("LuatVietnam — toàn văn", "https://luatvietnam.vn/thong-tin/quyet-dinh-06-qd-ttg-215370-d1.html"),
        ],
        None,
    ),
    "V.4": (
        "web",
        [
            ("Văn bản QPPL — QĐ 411/QĐ-TTg", "https://vanban.chinhphu.vn/?classid=2&docid=205555&pageid=27160"),
            ("Thư viện pháp luật — toàn văn", "https://thuvienphapluat.vn/van-ban/Thuong-mai/Quyet-dinh-411-QD-TTg-2022-phe-duyet-Chien-luoc-quoc-gia-phat-trien-kinh-te-so-va-xa-hoi-so-508672.aspx"),
        ],
        None,
    ),
    "V.5": (
        "web",
        [
            ("Công báo — QĐ 20/2025/QĐ-TTg", "https://congbao.chinhphu.vn/van-ban/quyet-dinh-so-20-2025-qd-ttg-45396.htm"),
            ("Thư viện pháp luật — toàn văn", "https://thuvienphapluat.vn/van-ban/Cong-nghe-thong-tin/Quyet-dinh-20-2025-QD-TTg-danh-muc-du-lieu-quan-trong-du-lieu-cot-loi-663548.aspx"),
        ],
        None,
    ),
    "V.6": (
        "web",
        [
            ("Văn bản QPPL — QĐ 2439/QĐ-TTg", "https://vanban.chinhphu.vn/?classid=2&docid=215785&pageid=27160"),
            ("Thư viện pháp luật — toàn văn", "https://thuvienphapluat.vn/van-ban/Cong-nghe-thong-tin/Quyet-dinh-2439-QD-TTg-2025-Khung-kien-truc-du-lieu-quoc-gia-Khung-quan-tri-du-lieu-quoc-gia-680001.aspx"),
        ],
        None,
    ),
    "V.7": (
        "web",
        [
            ("Cổng Chính phủ — QĐ 2711/QĐ-TTg", "https://chinhphu.vn/?docid=216205&pageid=27160"),
            ("LuatVietnam — toàn văn / phân tích", "https://luatvietnam.vn/chinh-sach/quyet-dinh-2711-qd-ttg-2025-phe-duyet-chien-luoc-phat-trien-doi-ngu-tri-thuc-den-2030-421523-d1.html"),
        ],
        None,
    ),
    "VI.1": (
        "partial",
        [
            ("NHNN — tin Chiến lược CĐS ngành NH (tham khảo)", "https://sbv.gov.vn/vi/w/sbv455211"),
            ("Banker.vn — tóm tắt QĐ 3579 (nguồn phụ)", "https://www.banker.vn/chien-luoc-chuyen-doi-so-nganh-ngan-hang-den-nam-2030"),
        ],
        "Chưa có link VBPL toàn văn QĐ 3579 công khai rõ ràng; tra cổng NHNN/VBPL khi cập nhật.",
    ),
    "VI.2": (
        "partial",
        [
            ("Banker.vn — tóm tắt QĐ 3580 (nguồn phụ)", "https://www.banker.vn/chien-luoc-du-lieu-nganh-ngan-hang-den-nam-2030"),
            ("Thời báo Ngân hàng — bài liên quan", "https://thoibaonganhang.vn/chuyen-doi-so-ngan-hang-xay-dung-co-so-du-lieu-dung-chung-tien-toi-ra-quyet-dinh-dua-tren-du-lieu-180727.html"),
        ],
        "Ưu tiên file PDF trên cổng NHNN / VBPL khi đăng tải.",
    ),
    "VI.3": (
        "web",
        [
            ("Công đoàn Ngân hàng VN — tài liệu", "https://vnubw.org.vn/Document/Detail/843"),
        ],
        "Văn bản Hiệp hội; đối chiếu khi có bản HHNH chính thức.",
    ),
    "VI.5": (
        "partial",
        [
            ("Cục An toàn thông tin — bài giới thiệu CT 02", "https://www.div.gov.vn/day-manh-chuyen-doi-so-va-dam-bao-an-ninh-an-toan-thong-tin-hoat-dong-ngan-hang-trong-nam-2026"),
            ("VBA — tin NHNN ban hành", "https://vnba.org.vn/vi/day-manh-chuyen-doi-so-va-bao-dam-an-ninh--an-toan-thong-tin-trong-hoat-dong-ngan-hang-nam-2026-20715.htm"),
        ],
        "Đối chiếu nguyên văn Chỉ thị trên cổng NHNN khi có.",
    ),
    "VI.6": (
        "partial",
        [
            ("VBA — tin QĐ 1938 & phong trào", "https://vnba.org.vn/vi/ngan-hang-nha-nuoc-ban-hanh-ke-hoach-cua-nganh-ngan-hang-trien-khai-phong-trao--binh-dan-hoc-vu-so-17509.htm"),
            ("VBA — xem văn bản (nếu mở được)", "https://vnba.org.vn/document/public-document/view?id=195&title=quyet-dinh-so-1938-qd-nhnn"),
        ],
        "Kiểm tra VBPL NHNN hoặc file PDF đính kèm tin NHNN.",
    ),
}

BADGE_LABEL = {
    "web": ("web", "Đã có nguồn web — chờ trích Điều"),
    "partial": ("partial", "Nguồn phụ / chờ bản gốc"),
}


def build_web_source(status: str, links: list[tuple[str, str]], note: str | None) -> str:
    cls = "web-source" + (" partial" if status == "partial" else "")
    lis = []
    for label, url in links:
        lis.append(
            f'<li><a href="{escape(url)}" target="_blank" rel="noopener noreferrer">{escape(label)}</a></li>'
        )
    note_html = ""
    if note:
        note_html = f'<p class="web-source-note">{escape(note)}</p>\n'
    return (
        f'        <div class="{cls}">\n'
        f'          <strong>Nguồn văn bản để trích Điều</strong>\n'
        f'          <p>Danh sách phục vụ tải bản toàn văn và đối chiếu (chi tiết trong <code>Nguon-van-ban-chuan.md</code>). '
        f'Cây Điều trong mind map sẽ bổ sung sau bước trích từ các URL.</p>\n'
        f"{note_html}"
        f'          <ul class="source-links">\n'
        + "".join(f"            {li}\n" for li in lis)
        + "          </ul>\n"
        f"        </div>"
    )


def patch_doc_card(html: str, card_id: str) -> str:
    if card_id not in PATCHES:
        return html
    status, links, note = PATCHES[card_id]
    badge_class, badge_text = BADGE_LABEL.get(status, ("need", "Cần OCR hoặc nguồn web chuẩn"))
    inner = build_web_source(status, links, note)

    block_re = re.compile(
        rf'(<article class="doc-card" id="{re.escape(card_id)}"[^>]*>)\s*'
        rf'(<header class="doc-head">.*?</header>)'
        rf'\s*.*?'
        rf'(</article>)',
        re.DOTALL,
    )

    def repl(m: re.Match[str]) -> str:
        open_tag = m.group(1)
        header = m.group(2)
        new_open = re.sub(r'data-status="[^"]*"', f'data-status="{status}"', open_tag)
        new_header = re.sub(
            r'<span class="status (?:need|ok|web|partial)">[^<]*</span>',
            f'<span class="status {badge_class}">{badge_text}</span>',
            header,
            count=1,
        )
        return new_open + "\n      " + new_header + "\n    \n" + inner + "\n        </article>"

    new_html, n = block_re.subn(repl, html, count=1)
    if not n:
        print(f"WARN: doc-card {card_id} not matched")
        return html
    return new_html


def patch_summary_status(html: str) -> str:
    """Replace status cell for patched codes."""

    def row_repl(code: str, status: str, label: str) -> None:
        nonlocal html
        badge_class, _ = BADGE_LABEL.get(status, ("need", ""))
        span = f'<span class="status {badge_class}">{escape(label)}</span>'
        pat = re.compile(
            rf'(<tr><td>{re.escape(code)}</td><td>[^<]*</td><td><span class="prio[^"]*">[^<]*</span></td><td>)'
            rf'<span class="status[^"]*">[^<]*</span>'
            rf'(</td>)',
        )
        html, n = pat.subn(r"\1" + span + r"\2", html, count=1)
        if not n:
            print(f"WARN: summary row not updated for {code}")

    for cid, (st, _, _) in PATCHES.items():
        _, lbl = BADGE_LABEL.get(st, ("need", "Cần OCR hoặc nguồn web chuẩn"))
        row_repl(cid, st, lbl)
    return html


def main() -> None:
    with open(HTML_PATH, encoding="utf-8") as f:
        html = f.read()

    for cid in PATCHES:
        html = patch_doc_card(html, cid)

    html = patch_summary_status(html)

    # CSS additions if missing
    extra_css = """
.web-source { margin:18px; padding:16px; border-radius:14px; border:1px solid #bfdbfe; background:#eff6ff; color:#1e3a5f; }
.web-source.partial { border-color:#fcd34d; background:#fffbeb; color:#78350f; }
.web-source-note { margin:10px 0 0; font-size:13px; color:#475569; }
.source-links { margin:10px 0 0 18px; }
.source-links a { color:#0369a1; font-weight:700; text-decoration:underline; }
.status.web { background:#dbeafe; color:#1e40af; }
"""
    if ".web-source {" not in html:
        html = html.replace(".need-source {", extra_css.strip() + "\n.need-source {")

    with open(HTML_PATH, "w", encoding="utf-8") as f:
        f.write(html)
    print("Patched", len(PATCHES), "cards + summary rows.")


if __name__ == "__main__":
    main()
