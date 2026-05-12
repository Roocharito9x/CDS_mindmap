#!/usr/bin/env python3
from __future__ import annotations

import html
import re
from collections import OrderedDict
from pathlib import Path
from typing import Iterable

import requests

HTML_PATH = Path(
    "/Users/ngochoang-ios/Downloads/BIDV AGENTIC 1.0/BMAD/docs/Tai lieu nang cao/Mindmaps-on-thi-chuyen-doi-so-v2-chi-tiet.html"
)

HEADERS = {"User-Agent": "Mozilla/5.0"}
TIMEOUT = 30

SOURCE_OVERRIDES: dict[str, list[str]] = {
    "I.6": ["https://dauthau.asia/van-ban-dau-thau/detail/Luat-Bao-ve-du-lieu-ca-nhan-cua-Quoc-hoi-610/"],
    "I.7": ["https://www.vietiso.com/blog/toan-van-luat-tri-tue-nhan-tao-2025-so-1342025qh15.html"],
    "II.2": ["https://thuvienphapluat.vn/van-ban/Tien-te-Ngan-hang/Nghi-dinh-94-2025-ND-CP-Co-che-thu-nghiem-co-kiem-soat-trong-linh-vuc-ngan-hang-584706.aspx"],
    "II.5": ["https://wincolaw.com.vn/vi/nghi-dinh-356-2025-nd-cp-ngay-31-12-2025-huong-dan-luat-bao-ve-du-lieu-ca-nhan.html"],
    "III.3": ["https://thuvienphapluat.vn/van-ban/Tien-te-Ngan-hang/Thong-tu-30-2025-TT-NHNN-sua-doi-Thong-tu-15-2024-TT-NHNN-675726.aspx"],
    "III.7": ["https://nhansu.vn/van-ban-phap-luat/Thong-tu-50-2024-TT-NHNN-an-toan-bao-mat-cung-cap-dich-vu-truc-tuyen-nganh-Ngan-hang-327954.html"],
    "III.9": ["https://nhansu.vn/van-ban-phap-luat/Thong-tu-64-2024-TT-NHNN-trien-khai-giao-dien-lap-trinh-ung-dung-mo-nganh-Ngan-hang-641360.html"],
    "IV.2": ["https://thuvienphapluat.vn/van-ban/Cong-nghe-thong-tin/Nghi-quyet-71-NQ-CP-2025-sua-doi-Chuong-trinh-hanh-dong-thuc-hien-Nghi-quyet-57-NQ-TW-650741.aspx"],
    "V.2": ["https://hethongphapluat.com/quyet-dinh-31-2021-qd-ttg-ve-quy-che-quan-ly-van-hanh-khai-thac-cong-dich-vu-cong-quoc-gia-do-thu-tuong-chinh-phu-ban-hanh.html"],
    "V.3": ["https://thuvienphapluat.vn/van-ban/Cong-nghe-thong-tin/Quyet-dinh-06-QD-TTg-2022-De-an-phat-trien-ung-dung-du-lieu-ve-dan-cu-2022-2025-499726.aspx?tab=1"],
    "V.7": ["https://hoatieu.vn/phap-luat/quyet-dinh-2711-qd-ttg-phe-duyet-chien-luoc-ve-phat-trien-doi-ngu-tri-thuc-den-nam-2030-tam-nhin-den-nam-2045-244891"],
    "VI.3": ["https://vnba.org.vn/vi/bo-chuan-muc-dao-duc-nghe-nghiep-va-quy-tac-ung-xu-cua-can-bo-ngan-hang-14.htm"],
}

MANUAL_FALLBACKS = {
    "II.4": {
        "structure": "section",
        "confidence": "secondary",
        "chapters": [
            {
                "label": "Phần I",
                "title": "PHẠM VI ĐIỀU CHỈNH",
                "unit_label": "mục",
                "items": [
                    {"label": "Mục 1", "title": "Chiến lược, kế hoạch về KHCN và ĐMST", "summary": "Quy định cách lập, phê duyệt và triển khai chiến lược, kế hoạch phục vụ tài chính và đầu tư cho khoa học, công nghệ, đổi mới sáng tạo."},
                    {"label": "Mục 2", "title": "Đối tượng và nguồn lực áp dụng", "summary": "Áp dụng cho cơ quan nhà nước, tổ chức nghiên cứu, doanh nghiệp, quỹ và chủ thể tham gia đầu tư cho khoa học, công nghệ, đổi mới sáng tạo."},
                ],
            },
            {
                "label": "Phần II",
                "title": "CƠ CHẾ TÀI CHÍNH, ĐẦU TƯ",
                "unit_label": "mục",
                "items": [
                    {"label": "Mục 1", "title": "Cơ cấu ngân sách và nội dung chi", "summary": "Làm rõ nguyên tắc bố trí ngân sách, nội dung chi và cơ chế quản lý, sử dụng kinh phí cho nhiệm vụ khoa học, công nghệ, đổi mới sáng tạo."},
                    {"label": "Mục 2", "title": "Quỹ phát triển KHCN và hỗ trợ đầu tư", "summary": "Quy định việc hình thành, quản lý, sử dụng các quỹ phát triển khoa học, công nghệ và cơ chế hỗ trợ đầu tư cho dự án đổi mới sáng tạo."},
                    {"label": "Mục 3", "title": "Ưu đãi, huy động nguồn lực xã hội", "summary": "Khuyến khích doanh nghiệp, tổ chức và khu vực tư nhân tham gia đầu tư, đồng tài trợ và chia sẻ rủi ro trong hoạt động đổi mới sáng tạo."},
                ],
            },
            {
                "label": "Phần III",
                "title": "TỔ CHỨC THỰC HIỆN",
                "unit_label": "mục",
                "items": [
                    {"label": "Mục 1", "title": "Trách nhiệm của cơ quan quản lý", "summary": "Phân công trách nhiệm cho cơ quan quản lý nhà nước trong hướng dẫn, kiểm tra, giám sát và tổng hợp kết quả thực hiện."},
                    {"label": "Mục 2", "title": "Bãi bỏ quy định cũ, hiệu lực thi hành", "summary": "Thay thế các cơ chế tài chính, đầu tư cũ không còn phù hợp, đồng thời xác lập hiệu lực áp dụng theo Nghị định mới."},
                ],
            },
        ],
    },
    "VI.1": {
        "structure": "section",
        "confidence": "secondary",
        "chapters": [
            {
                "label": "Phần I",
                "title": "MỤC TIÊU ĐẾN NĂM 2030",
                "unit_label": "mục",
                "items": [
                    {"label": "Mục 1", "title": "95% người dân có tài khoản giao dịch", "summary": "Phấn đấu 95% dân số từ 15 tuổi trở lên có tài khoản tại ngân hàng hoặc tổ chức được phép khác."},
                    {"label": "Mục 2", "title": "Thanh toán không dùng tiền mặt gấp 30 lần GDP", "summary": "Mở rộng quy mô thanh toán số, coi thanh toán không dùng tiền mặt là một chỉ tiêu lõi của chuyển đổi số ngành Ngân hàng."},
                    {"label": "Mục 3", "title": "80% giao dịch khách hàng qua kênh số", "summary": "Ưu tiên chuyển dịch hành vi giao dịch của khách hàng sang mobile banking, internet banking và các nền tảng số."},
                    {"label": "Mục 4", "title": "70% nghiệp vụ cho phép thực hiện hoàn toàn trên môi trường số", "summary": "Tiến tới số hóa end-to-end các nghiệp vụ có thể chuẩn hóa, cắt giảm bước thủ công và giấy tờ."},
                    {"label": "Mục 5", "title": "50% ngân hàng số hóa 100% quy trình cho vay nhỏ lẻ", "summary": "Đẩy mạnh chấm điểm tín dụng tự động, eKYC, tích hợp dữ liệu và phê duyệt số cho nhóm bán lẻ."},
                    {"label": "Mục 6", "title": "80% ngân hàng có doanh thu kênh số trên 30%", "summary": "Tăng hiệu quả kinh doanh số, mở rộng dịch vụ và hệ sinh thái số trong ngành."},
                ],
            },
            {
                "label": "Phần II",
                "title": "ĐỊNH HƯỚNG TRIỂN KHAI",
                "unit_label": "mục",
                "items": [
                    {"label": "Mục 1", "title": "Lấy người dân và doanh nghiệp làm trung tâm", "summary": "Thiết kế hành trình số dựa trên nhu cầu khách hàng, thuận tiện, an toàn và minh bạch."},
                    {"label": "Mục 2", "title": "Gắn chuyển đổi số với dữ liệu và AI", "summary": "Khai thác dữ liệu, trí tuệ nhân tạo và công nghệ mới để tối ưu vận hành, cá nhân hóa dịch vụ, phát hiện gian lận."},
                    {"label": "Mục 3", "title": "Bảo đảm an ninh, an toàn hệ thống", "summary": "Xem bảo mật, an toàn thông tin, liên tục dịch vụ và quản trị rủi ro là điều kiện tiên quyết của ngân hàng số."},
                ],
            },
        ],
    },
    "VI.2": {
        "structure": "section",
        "confidence": "secondary",
        "chapters": [
            {
                "label": "Phần I",
                "title": "MỤC TIÊU TỔNG QUÁT",
                "unit_label": "mục",
                "items": [
                    {"label": "Mục 1", "title": "Xác định dữ liệu là trung tâm của chuyển đổi số", "summary": "Dữ liệu được xem là nền tảng để điều hành, giám sát, cung ứng dịch vụ và đổi mới sáng tạo trong ngành Ngân hàng."},
                    {"label": "Mục 2", "title": "Kết nối, chia sẻ với CSDL quốc gia", "summary": "Thúc đẩy liên thông dữ liệu với CSDL quốc gia và các CSDL liên quan phục vụ Chính phủ số, kinh tế số, xã hội số."},
                    {"label": "Mục 3", "title": "Hỗ trợ phổ cập tài chính toàn diện", "summary": "Dữ liệu được khai thác để mở rộng tiếp cận dịch vụ ngân hàng, giảm ma sát và tăng tính liền mạch cho người dùng."},
                    {"label": "Mục 4", "title": "Dữ liệu trở thành tài sản chiến lược", "summary": "Phục vụ điều hành chính sách tiền tệ, quản lý nhà nước, phát triển sản phẩm dịch vụ ngân hàng số."},
                ],
            },
            {
                "label": "Phần II",
                "title": "TẦM NHÌN VÀ TRỤ CỘT",
                "unit_label": "mục",
                "items": [
                    {"label": "Mục 1", "title": "Liên thông dữ liệu toàn ngành", "summary": "Bảo đảm kết nối, chia sẻ dữ liệu giữa các đơn vị thuộc NHNN và giữa NHNN với các tổ chức tín dụng."},
                    {"label": "Mục 2", "title": "Bảo đảm an ninh, an toàn dữ liệu", "summary": "Quản trị vòng đời dữ liệu, phân quyền truy cập, bảo mật và kiểm soát tuân thủ là trụ cột bắt buộc."},
                    {"label": "Mục 3", "title": "Phát triển hạ tầng và nhân lực dữ liệu", "summary": "Xây dựng hạ tầng dữ liệu linh hoạt, bền vững, đồng thời phát triển nguồn nhân lực số chất lượng cao."},
                ],
            },
        ],
    },
    "VI.5": {
        "structure": "section",
        "confidence": "secondary",
        "chapters": [
            {
                "label": "Phần I",
                "title": "YÊU CẦU CHUYỂN ĐỔI SỐ NĂM 2026",
                "unit_label": "mục",
                "items": [
                    {"label": "Mục 1", "title": "Lồng ghép nhiệm vụ với chiến lược CĐS và dữ liệu ngành", "summary": "Các đơn vị cập nhật kế hoạch, nguồn lực và lộ trình phù hợp với Chiến lược chuyển đổi số ngành Ngân hàng và Chiến lược dữ liệu đến năm 2030."},
                    {"label": "Mục 2", "title": "Đẩy mạnh ứng dụng AI và công nghệ số", "summary": "Ưu tiên ứng dụng AI, dữ liệu và tự động hóa để phát hiện gian lận, tối ưu hóa quy trình nghiệp vụ, nâng cao trải nghiệm khách hàng."},
                    {"label": "Mục 3", "title": "Khai thác CSDL dân cư và VNeID", "summary": "Tiếp tục kết nối, khai thác dữ liệu dân cư, căn cước công dân gắn chip và VNeID phục vụ nghiệp vụ ngân hàng."},
                    {"label": "Mục 4", "title": "Thúc đẩy mô hình chi nhánh tự phục vụ", "summary": "Nghiên cứu mô hình self-service và chấm điểm tín dụng tự động dựa trên kho dữ liệu khách hàng và dữ liệu mở."},
                ],
            },
            {
                "label": "Phần II",
                "title": "AN NINH, AN TOÀN THÔNG TIN",
                "unit_label": "mục",
                "items": [
                    {"label": "Mục 1", "title": "Triển khai giải pháp an toàn, bảo mật cho ngân hàng điện tử", "summary": "Tuân thủ quy định pháp luật và văn bản chỉ đạo của NHNN đối với hoạt động ngân hàng điện tử và thanh toán trực tuyến."},
                    {"label": "Mục 2", "title": "Rà soát phương án an ninh mạng và bảo vệ dữ liệu", "summary": "Áp dụng tiêu chuẩn Việt Nam, quốc tế và giải pháp công nghệ tiên tiến cho các hệ thống thông tin trọng yếu."},
                    {"label": "Mục 3", "title": "Sao lưu, phục hồi, bảo đảm liên tục hoạt động", "summary": "Thực hiện nghiêm túc sao lưu, phục hồi dữ liệu và bảo đảm vận hành liên tục trước các phương thức tấn công mới."},
                    {"label": "Mục 4", "title": "Kiểm tra, đánh giá định kỳ và diễn tập sự cố", "summary": "Thường xuyên kiểm tra an toàn thông tin, khắc phục lỗ hổng, tổ chức diễn tập phương án ứng cứu sự cố."},
                    {"label": "Mục 5", "title": "Tăng cường giám sát và quản lý bên thứ ba", "summary": "Theo dõi chặt chẽ hạ tầng, dịch vụ CNTT của bên thứ ba để giảm rủi ro chuỗi cung ứng, nhất là khi dùng cloud."},
                ],
            },
        ],
    },
    "VI.6": {
        "structure": "section",
        "confidence": "secondary",
        "chapters": [
            {
                "label": "Phần I",
                "title": "MỤC TIÊU KẾ HOẠCH",
                "unit_label": "mục",
                "items": [
                    {"label": "Mục 1", "title": "Triển khai Kế hoạch 01-KH/BCĐTW trong ngành Ngân hàng", "summary": "Tổ chức thực hiện các quan điểm, mục tiêu, nhiệm vụ và giải pháp của ngành Ngân hàng được giao trong kế hoạch của Ban Chỉ đạo Trung ương."},
                    {"label": "Mục 2", "title": "Phổ cập tri thức và kỹ năng số", "summary": "Đưa phong trào Bình dân học vụ số vào hoạt động đào tạo, tuyên truyền, nâng cao năng lực số trong toàn ngành."},
                ],
            },
            {
                "label": "Phần II",
                "title": "TỔ CHỨC TRIỂN KHAI",
                "unit_label": "mục",
                "items": [
                    {"label": "Mục 1", "title": "Phân công nhiệm vụ cho đơn vị thuộc NHNN và cơ sở đào tạo", "summary": "Xác định nhiệm vụ cụ thể cho các đơn vị thuộc NHNN, Học viện Ngân hàng, Đại học Ngân hàng TP.HCM, BHTGVN và doanh nghiệp do NHNN quản lý."},
                    {"label": "Mục 2", "title": "Giao trách nhiệm cho TCTD và chi nhánh ngân hàng nước ngoài", "summary": "Lồng ghép nhiệm vụ phổ cập số vào kế hoạch đơn vị, bảo đảm mỗi tổ chức có phương án triển khai phù hợp."},
                ],
            },
        ],
    },
}

TAG_RULES = OrderedDict(
    [
        ("bank", (["ngân hàng", "tổ chức tín dụng", "chi nhánh ngân hàng", "nhnn", "học viện ngân hàng"], "BANK")),
        ("pay", (["thanh toán", "thẻ", "api", "open api", "ví", "chuyển tiền", "tài khoản thanh toán"], "PAY")),
        ("sec", (["an toàn", "an ninh", "bảo mật", "rủi ro", "mã hóa", "an ninh mạng"], "SEC")),
        ("data", (["dữ liệu", "thông tin", "định danh", "định danh điện tử", "dân cư", "cơ sở dữ liệu"], "DATA")),
        ("digital", (["số", "điện tử", "trực tuyến", "chuyển đổi số", "công nghệ số", "vneid"], "DIGITAL")),
        ("innov", (["đổi mới sáng tạo", "ai", "trí tuệ nhân tạo", "sandbox", "khoa học, công nghệ", "khoa học công nghệ", "nhân lực"], "INNOV")),
        ("gov", (["quản lý", "trách nhiệm", "kế hoạch", "mục tiêu", "chỉ tiêu", "tổ chức thực hiện", "đạo đức", "tài chính"], "GOV")),
    ]
)

DOC_TAG_HINTS = {
    "ngân hàng": "bank",
    "thanh toán": "pay",
    "thẻ": "pay",
    "api": "pay",
    "attt": "sec",
    "dữ liệu": "data",
    "định danh": "data",
    "cđs": "digital",
    "dịch vụ công": "digital",
    "kinh tế số": "digital",
    "đmst": "innov",
    "ai": "innov",
    "nhân lực": "innov",
    "quản trị": "gov",
    "đạo đức": "gov",
    "kế toán": "gov",
    "tài chính": "gov",
}


def clean_text(raw: str) -> str:
    text = re.sub(r"(?is)<[^>]+>", " ", raw)
    text = html.unescape(text).replace("\xa0", " ")
    text = re.sub(r"\s+", " ", text).strip()
    return text


def html_to_lines(src: str) -> list[str]:
    src = re.sub(r"(?is)<(script|style).*?>.*?</\1>", " ", src)
    src = re.sub(r"(?i)<br\s*/?>", "\n", src)
    src = re.sub(r"(?i)</(p|div|li|tr|h1|h2|h3|h4|h5|h6|section|article|ul|ol|table|blockquote|td)>", "\n", src)
    src = re.sub(r"(?is)<[^>]+>", " ", src)
    src = html.unescape(src).replace("\xa0", " ")
    lines = []
    for line in src.splitlines():
        line = re.sub(r"\s+", " ", line).strip()
        if line:
            lines.append(line)
    return lines


def split_heading(heading: str, default_label: str) -> tuple[str, str]:
    heading = clean_text(heading)
    m = re.match(r"^((?:Chương|Phần|Mục)\s+[^\s]+|[IVXLC]+\s*[-\.])\s*(.*)$", heading, re.I)
    if m:
        return m.group(1).strip(), m.group(2).strip(" .:-")
    return default_label, heading


def normalize_summary(lines: Iterable[str], title: str) -> str:
    clean_lines = []
    for line in lines:
        line = re.sub(r"^\d+\.\s*", "", line).strip(" .;:-")
        if not line:
            continue
        if line.lower() == title.lower():
            continue
        clean_lines.append(line)
        if len(clean_lines) >= 2:
            break
    return " ".join(clean_lines) if clean_lines else title


def extract_tags(text: str, doc_tags: list[str]) -> list[tuple[str, str]]:
    text_l = text.lower()
    found: list[tuple[str, str]] = []
    for css, (keywords, label) in TAG_RULES.items():
        if any(keyword in text_l for keyword in keywords):
            found.append((css, label))
    if not found:
        for tag in doc_tags:
            hint = DOC_TAG_HINTS.get(tag.lower())
            if hint and hint in TAG_RULES:
                found.append((hint, TAG_RULES[hint][1]))
    uniq = []
    seen = set()
    for item in found:
        if item[0] in seen:
            continue
        uniq.append(item)
        seen.add(item[0])
    return uniq[:4]


def item_from_heading(label: str, title: str, body_lines: list[str], doc_tags: list[str]) -> dict:
    summary = normalize_summary(body_lines, title)
    tags = extract_tags(f"{title} {summary}", doc_tags)
    return {"label": label, "title": title, "summary": summary, "tags": tags}


def parse_anchor_articles(src: str, doc_tags: list[str]) -> list[dict]:
    chapters = []
    chapter_defs = []
    for match in re.finditer(r'(?is)<a[^>]+name="(chuong_[^"]+)"[^>]*>(.*?)</a>', src):
        key = match.group(1)
        if key.endswith("_name"):
            continue
        label = clean_text(match.group(2))
        title_match = re.search(r'(?is)<a[^>]+name="%s_name"[^>]*>(.*?)</a>' % re.escape(key), src[match.end() : match.end() + 2000])
        title = clean_text(title_match.group(1)) if title_match else ""
        chapter_defs.append((match.start(), label, title))
    article_matches = [m for m in re.finditer(r'(?is)<a[^>]+name="dieu_[^"]*"[^>]*>(.*?)</a>', src) if re.match(r"^Điều\s+\d+", clean_text(m.group(1)))]
    if not article_matches:
        return []
    chapter_idx = 0
    current_key = ("Không phân chương", "")
    chapter_map: OrderedDict[tuple[str, str], list[dict]] = OrderedDict()
    for idx, match in enumerate(article_matches):
        while chapter_idx < len(chapter_defs) and chapter_defs[chapter_idx][0] < match.start():
            current_key = (chapter_defs[chapter_idx][1], chapter_defs[chapter_idx][2])
            chapter_idx += 1
        heading = clean_text(match.group(1))
        article_m = re.match(r"^Điều\s+(\d+)\.?\s*(.*)$", heading)
        if not article_m:
            continue
        label = f"Điều {article_m.group(1)}"
        title = article_m.group(2).strip() or label
        end = article_matches[idx + 1].start() if idx + 1 < len(article_matches) else len(src)
        segment = src[match.end() : end]
        paras = [clean_text(p) for p in re.findall(r"(?is)<p[^>]*>(.*?)</p>", segment)]
        body_lines = [p for p in paras if p and not p.startswith(("Chương ", "Mục ", "PHỤ LỤC"))]
        chapter_map.setdefault(current_key, []).append(item_from_heading(label, title, body_lines, doc_tags))
    for i, ((label, title), items) in enumerate(chapter_map.items(), 1):
        chapters.append({"label": label or f"Phần {i}", "title": title, "unit_label": "Điều", "items": items})
    return chapters


def parse_section_items(lines: list[str], doc_tags: list[str], label_prefix: str = "Mục") -> list[dict]:
    items = []
    current = None
    extra_idx = 1
    for line in lines:
        num_m = re.match(r"^(\d+)\.\s*(.*)$", line)
        bullet_m = re.match(r"^[-•]\s*(.*)$", line)
        if num_m:
            if current:
                items.append(item_from_heading(current["label"], current["title"], current["body"], doc_tags))
            current = {"label": f"{label_prefix} {num_m.group(1)}", "title": num_m.group(2).strip() or f"{label_prefix} {num_m.group(1)}", "body": []}
        elif bullet_m:
            if current:
                current["body"].append(bullet_m.group(1).strip())
            else:
                items.append(item_from_heading(f"Ý {extra_idx}", bullet_m.group(1).strip(), [], doc_tags))
                extra_idx += 1
        else:
            if current:
                current["body"].append(line)
    if current:
        items.append(item_from_heading(current["label"], current["title"], current["body"], doc_tags))
    return items


def parse_anchor_sections(src: str, doc_tags: list[str]) -> list[dict]:
    section_matches = list(re.finditer(r'(?is)<a[^>]+name="muc_[^"]*"[^>]*>(.*?)</a>', src))
    if len(section_matches) < 2:
        return []
    chapters = []
    for idx, match in enumerate(section_matches):
        heading = clean_text(match.group(1))
        label, title = split_heading(heading, f"Phần {idx + 1}")
        end = section_matches[idx + 1].start() if idx + 1 < len(section_matches) else len(src)
        lines = html_to_lines(src[match.end() : end])
        items = parse_section_items(lines, doc_tags)
        if items:
            chapters.append({"label": label, "title": title, "unit_label": "mục", "items": items})
    return chapters


def parse_plain_articles(lines: list[str], doc_tags: list[str]) -> list[dict]:
    chapters: OrderedDict[tuple[str, str], list[dict]] = OrderedDict()
    current_ch = ("Không phân chương", "")
    current_item = None
    idx = 0
    while idx < len(lines):
        line = lines[idx]
        if re.match(r"^Chương\s+[IVXLC]+\b", line):
            title = ""
            if idx + 1 < len(lines) and not re.match(r"^(Điều|Chương|Mục)\s+", lines[idx + 1]):
                title = lines[idx + 1]
                idx += 1
            current_ch = (line, title)
            idx += 1
            continue
        m = re.match(r"^Điều\s+(\d+)[\.:]?\s*(.*)$", line)
        if m:
            if current_item:
                chapters.setdefault(current_ch, []).append(item_from_heading(current_item["label"], current_item["title"], current_item["body"], doc_tags))
            current_item = {"label": f"Điều {m.group(1)}", "title": m.group(2).strip() or f"Điều {m.group(1)}", "body": []}
        elif current_item:
            current_item["body"].append(line)
        idx += 1
    if current_item:
        chapters.setdefault(current_ch, []).append(item_from_heading(current_item["label"], current_item["title"], current_item["body"], doc_tags))
    out = []
    for i, ((label, title), items) in enumerate(chapters.items(), 1):
        out.append({"label": label or f"Phần {i}", "title": title, "unit_label": "Điều", "items": items})
    return out


def parse_plain_sections(lines: list[str], doc_tags: list[str]) -> list[dict]:
    chapters = []
    current = None
    for line in lines:
        if re.match(r"^[IVXLC]+\s*[-\.]\s+", line):
            if current and current["items"]:
                chapters.append(current)
            label, title = split_heading(line, f"Phần {len(chapters) + 1}")
            current = {"label": label, "title": title, "unit_label": "mục", "items": []}
            continue
        if current is None:
            continue
        if re.match(r"^\d+\.\s+", line) or re.match(r"^[-•]\s*", line):
            current["items"].append(line)
    out = []
    for chapter in chapters + ([current] if current and current["items"] else []):
        items = parse_section_items(chapter["items"], doc_tags)
        if items:
            out.append({"label": chapter["label"], "title": chapter["title"], "unit_label": "mục", "items": items})
    return out


def choose_structure(src: str, doc_id: str, doc_tags: list[str]) -> tuple[list[dict], str, str]:
    article_chapters = parse_anchor_articles(src, doc_tags)
    section_chapters = parse_anchor_sections(src, doc_tags)
    if not article_chapters:
        lines = html_to_lines(src)
        article_chapters = parse_plain_articles(lines, doc_tags)
        if not section_chapters:
            section_chapters = parse_plain_sections(lines, doc_tags)
    article_count = sum(len(ch["items"]) for ch in article_chapters)
    section_count = sum(len(ch["items"]) for ch in section_chapters)
    if article_chapters and (article_count > 5 or not section_chapters):
        return article_chapters, "article", "primary"
    if article_chapters and section_chapters:
        first = {"label": "Phần I", "title": "QUYẾT ĐỊNH / VĂN BẢN BAN HÀNH", "unit_label": "Điều", "items": [item for chapter in article_chapters for item in chapter["items"]]}
        return [first] + section_chapters, "mixed", "primary"
    if section_chapters:
        return section_chapters, "section", "primary"
    if article_chapters:
        return article_chapters, "article", "primary"
    if doc_id in MANUAL_FALLBACKS:
        info = MANUAL_FALLBACKS[doc_id]
        return info["chapters"], info["structure"], info["confidence"]
    return [], "article", "primary"


def badge_html(tags: list[tuple[str, str]]) -> str:
    return "".join(f'<span class="mini {css}">{label}</span>' for css, label in tags)


def render_mind_tree(chapters: list[dict]) -> str:
    parts = ['<div class="mind-tree">']
    for chapter in chapters:
        items = chapter["items"]
        parts.append(f'<details class="chapter" open><summary><span>{html.escape(chapter["label"])}</span><strong>{html.escape(chapter["title"])}</strong><em>{len(items)} {html.escape(chapter["unit_label"])}</em></summary><div class="article-list">')
        for item in items:
            item_tags = item.get("tags", [])
            bullets = [item.get("title", ""), item.get("summary", "")]
            bullet_html = "".join(f"<li>{html.escape(b)}</li>" for b in bullets if b)
            parts.append(
                f'<details class="article"><summary><span class="article-num">{html.escape(item["label"])}</span><span>{html.escape(item.get("title", ""))}</span>{badge_html(item_tags)}</summary><ul>{bullet_html}</ul></details>'
            )
        parts.append("</div></details>")
    parts.append("</div>")
    return "".join(parts)


def render_review_table(chapters: list[dict], structure: str) -> str:
    items = [item for chapter in chapters for item in chapter["items"]]
    rows = items[:12]
    header_suffix = "Điều liên quan ngân hàng/CĐS" if structure == "article" else "mục chính"
    row_html = "".join(
        f"<tr><td>{html.escape(item['label'])}</td><td>{html.escape(item.get('title', ''))} — {html.escape(item.get('summary', ''))}</td><td>{html.escape(', '.join(label for _, label in item.get('tags', [])))}</td></tr>"
        for item in rows
    )
    return f'<div class="review-table"><h4>Bảng ôn nhanh theo {header_suffix}</h4><table><thead><tr><th>Điều</th><th>Nội dung cần nhớ</th><th>Nhãn</th></tr></thead><tbody>{row_html}</tbody></table></div>'


def update_status_badge(header: str, structure: str, confidence: str) -> str:
    if confidence == "secondary":
        cls, text = "partial", "Mind map cấu trúc từ nguồn phụ" if structure != "article" else "Mind map từ nguồn phụ"
    elif structure != "article":
        cls, text = "ok", "Đã trích mind map cấu trúc"
    else:
        cls, text = "ok", "Đã trích tới Điều"
    return re.sub(r'<span class="status [^"]+">[^<]*</span>', f'<span class="status {cls}">{text}</span>', header, count=1)


def update_meta_line(header: str, count: int, structure: str) -> str:
    count_text = f"{count} Điều" if structure == "article" else f"{count} mục cấu trúc"
    return re.sub(
        r'(<div class="meta-line">.*?</code>\s*·\s*)(.*?)(\s*·\s*điểm đọc:)',
        lambda m: m.group(1) + count_text + m.group(3),
        header,
        count=1,
        flags=re.S,
    )


def set_or_replace_attr(tag: str, attr: str, value: str) -> str:
    if re.search(rf'{attr}="[^"]*"', tag):
        return re.sub(rf'{attr}="[^"]*"', f'{attr}="{value}"', tag)
    return tag[:-1] + f' {attr}="{value}">'


def update_open_tag(tag: str, structure: str, confidence: str) -> str:
    tag = set_or_replace_attr(tag, "data-status", "partial" if confidence == "secondary" else "ok")
    if structure != "article":
        tag = set_or_replace_attr(tag, "data-structure", structure)
    if confidence == "secondary":
        tag = set_or_replace_attr(tag, "data-source-confidence", "secondary")
    return tag


def source_candidates(card_id: str, block: str) -> list[str]:
    urls = [html.unescape(u) for u in SOURCE_OVERRIDES.get(card_id, [])]
    urls.extend(html.unescape(u) for u in re.findall(r'<a href="([^"]+)"', block))
    seen = set()
    out = []
    for url in urls:
        if url in seen:
            continue
        seen.add(url)
        out.append(url)
    return out


def fetch_best_structure(card_id: str, block: str, doc_tags: list[str]) -> tuple[list[dict], str, str]:
    for url in source_candidates(card_id, block):
        try:
            src = requests.get(url, timeout=TIMEOUT, headers=HEADERS).text
        except Exception:
            continue
        chapters, structure, confidence = choose_structure(src, card_id, doc_tags)
        item_count = sum(len(ch["items"]) for ch in chapters)
        if item_count >= 3:
            return chapters, structure, confidence
    if card_id in MANUAL_FALLBACKS:
        info = MANUAL_FALLBACKS[card_id]
        return info["chapters"], info["structure"], info["confidence"]
    return [], "article", "primary"


def patch_card_block(block: str) -> str:
    card_id = re.search(r'id="([^"]+)"', block).group(1)
    doc_tags = [t.strip() for t in (re.search(r'data-tags="([^"]*)"', block).group(1).split(","))]
    open_tag = re.search(r"(<article class=\"doc-card\"[^>]*>)", block).group(1)
    header = re.search(r"(<header class=\"doc-head\">.*?</header>)", block, re.S).group(1)
    source_match = re.search(r'(<div class="web-source.*?</div>)', block, re.S)
    source_block = source_match.group(1) if source_match else ""
    chapters, structure, confidence = fetch_best_structure(card_id, block, doc_tags)
    if not chapters:
        return block
    open_tag = update_open_tag(open_tag, structure, confidence)
    header = update_status_badge(header, structure, confidence)
    header = update_meta_line(header, sum(len(ch["items"]) for ch in chapters), structure)
    new_body = render_mind_tree(chapters) + render_review_table(chapters, structure)
    if source_block:
        new_body += source_block
    return f"{open_tag}\n      {header}\n    {new_body}\n        </article>"


def main() -> None:
    html_text = HTML_PATH.read_text(encoding="utf-8")
    blocks = re.findall(r'<article class="doc-card".*?</article>', html_text, flags=re.S)
    updated = 0
    for block in blocks:
        if '<div class="mind-tree">' in block:
            continue
        new_block = patch_card_block(block)
        if new_block != block:
            html_text = html_text.replace(block, new_block, 1)
            updated += 1
    HTML_PATH.write_text(html_text, encoding="utf-8")
    print(f"Updated {updated} missing doc cards.")


if __name__ == "__main__":
    main()
