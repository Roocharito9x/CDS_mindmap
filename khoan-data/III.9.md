# III.9 — Thông tư 64/2024/TT-NHNN — Open API ngân hàng

## Điều 1. Phạm vi điều chính
1. Thông tư này quy định về việc triển khai giao diện lập trình ứng dụng mở trong ngành Ngân hàng.
2. Thông tư này không điều chỉnh việc kết nối, xử lý dữ liệu chứa thông tin thuộc phạm vi bí mật nhà nước. Việc xử lý đữ liệu chứa thông tin thuộc : , phạm vi bí mật nhà nước được thực hiện theo quy định của pháp luật hiện hành.
3. Thông tư này không điều chỉnh việc kết nối, xử lý dữ liệu trực tiếp giữa: qua giao diện lập trình ứng dụng để phục vụ nghiệp vụ nội bộ của chính tỗ chức đó; chủ trì hệ thống bù trừ điện tử. Tô chức chủ trì hệ thống bù trừ điện tử được xác định theo quy định của Ngân hàng Nhà nước Việt Nam về hoạt động cung ứng dịch vụ trung gian thanh toán.
  - a) Hệ thống thông tin của Ngân hàng và hệ thống thông tin của tô chức
  - b) Hệ thống thông tin của Ngân hàng và hệ thống thông tin của Tổ chức

## Điều 2. Đối tượng áp dụng
1. Ngân hàng thương mại, ngân hàng hợp tác xã, chí nhánh ngân hàng nước ngoài (sau đây gọi chung là Ngân hàng).
2. Tố chức, cá nhân có liên quan trong việc triển khai dịch vụ qua giao diện lập trình ứng dụng mở trong ngành ngân hàng.

## Điều 3. Giải thích từ ngữ
2. Giao diện lập trình ứng dụng mở trong ngành Ngân hàng (Open API) là tập hợp các API được Ngân hàng cung cấp cho bên thứ ba trực tiếp kết nối, xử lý dữ liệu để cung ứng dịch vụ cho khách hàng. Open API gồm: Open API cơ bản và Open API khác.
3. Hệ thống thử nghiệm Open API là hệ thống thông tin của Ngân hàng cung cấp cho bên thứ ba để thử nghiệm các Open API trước khi triển khai chính thức.
4. Khách hàng là cá nhân sử dụng dịch vụ của Ngân hàng. 3
5. Bên thứ ba là tô chức hoặc Ngân hàng khác có thỏa thuận bằng hợp đồng với Ngân hàng trong việc kết nói, xử lý dữ liệu qua Open API đề cung ứng dịch vụ cho khách hàng.
6. Sự đồng ý của khách hàng là việc thê hiện rõ ràng, tự nguyện, khăng định việc cho phép xử lý dữ liệu cá nhân của khách hàng.

## Điều 4. Nguyên tắc chung
1. Tuân thủ các quy định của pháp luật về giữ bí mật, cung cấp thông tin khách hàng và bảo vệ dữ liệu cá nhân. Việc xử lý dữ liệu cá nhân của khách hàng chỉ phục vụ cho chính khách hàng đó, trừ trường hợp theo quy dịnh của pháp luật.
2. Dữ liệu trong quá trình xử lý phải được quản lý, lưu trữ, khai thác, sử dụng đúng mục đích tại hợp dồng giữa các bên và phù hợp với quy định của pháp luật.
3. Dữ liệu trong quá trình xử lý phải bảo đảm tính cập nhật và chính xác. Trường hợp có sai lệch phải thực hiện đính chính, hiệu chỉnh kịp thời theo thỏa thuận giữa các bên. Chương II QUY ĐỊNH CỤ THẺ VẺ TRIÊN KHAI OPEN API Mục I QUY ĐỊNH TRIÊN KHAI OPEN API

## Điều 5. Nguyên tắc triển khai Open API
1. Khi triên khai Open API cơ bản quy dịnh tại Điều 6 Thông tư này. Ngân hàng phải tuân thủ quy định tại Phụ lục 01, Phụ lục 02 ban hành kèm theo Thông tư này.
2. Khi triển khai Open API khác theo nhu cầu thực tế và phù hợp quy định của pháp luật ngoài danh mục Open API quy định tại Điều 6 Thông tư này, Ngân hàng phải tuân thủ quy định tại Phụ lục 02 ban hành kèm theo Thông tư này. l
3. Ngân hàng chỉ được phép triển khai Open API quy định tại điểm c khoản 1 Diều 6 cho bên thứ ba là Ngân hàng. tổ chức cung ứng dịch vụ trung gian thanh toán.

## Điều 6. Danh mục Open API
1. Danh mục Open API cơ bản được tô chức thành các nhóm sau: Lấy thông tin lãi suất, API Lấy thông tin tỷ giá; lấy sự đồng ý của khách hàng, API Lấy mã truy cập, API Làm mới mã truy cập, API Thu hồi mã truy cập, API Lấy danh sách tài khoản, API Lấy thông tin tài khoản, API Lấy lịch sử giao dịch; ví điện tử gồm: () Open API khởi tạo thanh toán gồm: API Khởi tạo thanh toán, API Xác nhận khách hàng Luồng Redirect, API Lấy mã truy cập luồng Redireet. API Cập nhật trạng thái xác nhận thanh toán của khách hàng luồng
  - a) Open API truy vấn thông tin tỷ giá, lãi suất của Ngân hàng gồm: API
  - c) Open API khởi tạo thanh toán, nạp tiền vào ví điện tử, rút tiền ra khỏi
2. Chỉ tiết đặc tả danh mục Open API tại khoản 1 Điều này được quy định cụ thê tại Phụ lục 01 ban hành kèm theo Thông tư nảy.

## Điều 7. Danh mục tiêu chuẩn kỹ thuật
1. Các tiêu chuẩn kỹ thuật triển khai Open API gồm tiêu chuẩn kiến trúc, tiêu chuẩn đữ liệu và tiêu chuẩn an toàn thông tin.
2. Tiêu chuẩn kỹ thuật triển khai Open API trong ngành Ngân hàng quy định cụ thẻ tại Phụ lục 02 ban hành kèm theo Thông tư này.

## Điều 8. Hợp đồng giữa Ngân hàng với bên thứ ba
1. Cam kết bảo mật thông tin, trong đó có thỏa thuận về việc bảo đảm an toàn, bảo mật thông tn khi thực hiện xử lý dữ liệu qua Open API do Ngân hàng cung cấp.
2. Cam kết sử dụng dữ liệu do Ngân hàng cung cấp dúng phạm vi, mục đích.
3. Bên thứ ba phải thông báo cho Ngân hàng khi phát hiện nhân sự vì phạm quy định về an toàn thông tin mạng khi triển khai Open API.
4. Thông tin về dịch vụ cung cấp cho khách hàng được triển khai qua Open API.
5. Thông tin về phí dịch vụ cung cấp cho khách hàng được triển khai qua Open API (nêu có).
6. Điều khoản về hệ thống thông tin của bên thứ ba kết nói, xử lý dữ liệu qua Open API phải được đánh giá, xác định cấp độ theo quy định của Chính phủ về bảo đảm an toàn hệ thống thông tin theo cấp độ.
7. Quyên truy cập dữ liệu của bên thứ ba khi triển khai Open API.
8. Diều khoản chấm dứt hợp đồng.

## Điều 9. Công khai thông tin Open API
1. Thông tin về Hệ thông thử nghiệm Open API.
2. Danh mục các Open API Ngân hàng triển khai. Mục 2 QUYÊN VÀ TRÁCH NHIỆM CỦA NGÂN HÀNG VÀ BÊN THỨ BA

## Điều 10. Quyền của Ngân hàng
1. Yêu cầu bên thứ ba cung cấp các thông tin cần thiết liên quan đến quá trình kết nối, xử lý đữ liệu qua Open API. : l
2. Các quyền khác quy định trong hợp dòng với bên thứ ba.

## Điều 11. Trách nhiệm của Ngân hàng
1. Hoàn thiện cơ sở hạ tầng hệ thống thông tin phục vụ triển khai Open API để sẵn sàng kết nói, xử lý dữ liệu.
2. Xây dựng và hoàn thiện các tài liệu hướng dẫn kết nồi, xử lý dữ liệu.
3. Bảo đảm chất lượng đữ liệu trong quá trình triển khai Open API. Thông báo kịp thời cho bên thứ ba khi có sai lệch dữ liệu và phôi hợp với bên thứ ba đính chính, hiệu chính kịp thời.
4. Bảo đảm an toàn, an ninh mạng cho hệ thống thông tin triển khai Open API, đáp ứng tối thiểu cấp độ 3 theo quy định của Chính phủ về bảo đảm an toàn hệ thống thông tin theo cấp độ và tuân thủ quy định của Ngân hàng Nhà nước Việt Nam về an toàn hệ thống thông tin trong hoạt động ngân hàng.
5. Cung cấp công cụ hoặc chức năng cho phép khách hàng thực hiện: 8) Tra cứu các dữ liệu mà khách hàng dồng ý cho bên thứ ba xử lý;
  - b) Rút lại sự đồng ý của khách hàng theo quy định của pháp luật.
6. Thiết lập thời hạn được thực hiện truy vấn thông tin của khách hàng sau khi được khách hàng đồng ý không quả 180 ngày, trừ trường hợp có thỏa thuận khác giữa khách hàng với Ngân hàng.
7. Cung cấp thông tin tình hình triển khai Open API cho Ngân hàng Nhà nước Việt Nam (thông qua Cục Công nghệ thông tin) khi dược yêu câu.
8. Phối hợp với bên thứ ba theo thỏa thuận và với cơ quan có thâm quyền để giải quyết vướng mắc, tranh chấp trong quá trình triên khai Open API.
9. Có giải pháp công nghệ giới hạn số lần truy vấn tự động thông tin của khách hàng từ bên thứ ba.
10. Chịu trách nhiệm lựa chọn, thầm định, giám sát và quản lý bên thứ ba.
11. Thực hiện cập nhật hoặc thu hồi quyền truy cập dữ liệu của bên thứ ba khi có thay đổi theo hợp đồng.
12. Giám sát hoạt động truy cập: 7 bât thường hoặc trái phép từ bên thứ ba; trong vòng 03 tháng và sao lưu tôi thiểu 01 năm để phục vụ kiêm tra khi cần thiết.
  - a) Có hệ thống giám sát đề phát hiện và ngăn chặn các hành vi truy cập
  - b) Ghi nhật ký toàn bộ việc sử dụng Open API từ bên thứ ba tối thiêu

## Điều 12. Quyền và trách nhiệm của bên thứ ba
1. Bên thứ ba có các quyên theo hợp đồng hoặc thỏa thuận với Ngân hàng, khách hàng.
2. Trách nhiệm của bên thứ ba: tuyên: (1) Tra cứu các dữ liệu mà khách hàng đồng ý cho bên thứ ba xử lý; (ï) Rút lại sự đồng ý của khách hàng theo quy định của pháp luật. dịch vụ và hướng dẫn khách hàng cách thức sử dụng dịch vụ. quy trình xử lý khiếu nại; quy trình giải quyết tranh chấp; quy trình bảo đảm hoạt động liên tục và quy trình sử dụng dịch vụ khi cung cấp địch vụ cho khách hàng. bên và theo quy định của pháp luật. thông tin, an toàn thông tin khi triển khai Open API. Hình thức và thời gian
  - a) Cung cấp công cụ hoặc chức năng cho phép khách hàng thực hiện trực
  - b) Thông báo cho khách hàng các điều khoản, điều kiện về việc sử dụng
  - e) Ban hành quy trình quản lý rủi ro; quy trình chăm sóc khách hàng;
  - đ) Khai thác và sử dụng dữ liệu đúng phạm vi theo thỏa thuận giữa các
  - đ) Thông báo kịp thời cho Ngân hàng khi xảy ra sự cô về công nghệ
  - e) Thông báo kịp thời cho Ngân hàng khi có sai lệch dữ liệu và phối hợp

## Điều 13. Trách nhiệm của Cục Công nghệ thông tin
1. Chủ trì, phối hợp với các đơn vị liên quan thuộc Ngân hàng Nhà nước Việt Nam xử lý các vướng mắc phát sinh trong quá trình thực hiện Thông tư này.
2. Theo dõi, tổng hợp, báo cáo Thống dốc Ngân hàng Nhà nước tình hình thực hiện của các Ngân hàng theo quy định tại Thông tư này.
3. Kiêm tra Ngân hàng trong việc thực hiện Thông tư này.

## Điều 14. Hiệu lực thi hành

Thông tư này có hiệu lực thi hành kể từ ngày 01 tháng 3 năm 2025.

## Điều 15. Điều khoản chuyển tiếp
1. Lập danh mục API, Open API đang triển khai và kế hoạch thực hiện chi tiết bảo đâm tuân thủ quy định Thông tư này gửi Ngân hàng Nhà nước Việt Nam (thông qua Cục Công nghệ thông tin), hoàn thành trước ngày 01 tháng 07 năm 2025.
2. Tuân thủ các quy định tại Thông tư này, hoàn thành trước ngày 01 tháng 3 năm 2027.

## Điều 16. Tổ chức thực hiện

Thủ trưởng các đơn vị thuộc Ngân hàng Nhà nước Việt Nam, ngân hàng thương mại, ngân hàng hợp tác xã, chi nhánh ngân hàng nước ngoài chịu trách nhiệm tổ chức thực hiện Thông tư này.
