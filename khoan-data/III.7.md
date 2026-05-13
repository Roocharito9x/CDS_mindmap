# III.7 — TT 50/2024/TT-NHNN — An toàn bảo mật dịch vụ trực tuyến ngân hàng


## Điều 1. Phạm vi điều chỉnh và đối
1. tượng áp dụng
1. Phạm vi điều chỉnh
   - a) Hoạt động ngân hàng và các hoạt động kinh doanh
   - b) Hoạt động cung ứng dịch vụ trung gian thanh
   - c) Hoạt động thông tin tín dụng.
2. Đối tượng áp dụng
1. Thông tư này áp dụng đối với các tổ chức tín dụng, chi nhánh ngân hàng nước ngoài, tổ chức cung ứng dịch vụ trung gian thanh toán, công ty thông tin tín dụng (sau đây gọi chung là đơn vị).

## Điều 2. Giải thích từ ngữ và
1. thuật ngữ Trong Thông tư này, các từ ngữ dưới đây được hiểu như sau:
1. Dịch vụ trực tuyến trong ngành Ngân hàng
1. (gọi tắt là dịch vụ Online Banking) là dịch vụ quy định tại khoản 1 Điều 1 Thông tư này được các đơn vị cung cấp cho khách hàng trên môi trường mạng để thực hiện các giao dịch điện tử (gọi tắt là giao dịch), không bao gồm các giao dịch trực tiếp tại các đơn vị chấp nhận thanh toán qua thiết bị chấp nhận thẻ tại điểm bán, qua Mã phản hồi nhanh (Quick Response Code - QR Code) hiển thị từ phía khách hàng.
2. Hệ thống Online Banking là một tập hợp có
1. cấu trúc các trang thiết bị phần cứng, phần mềm, cơ sở dữ liệu, hệ thống mạng truyền thông và an toàn, bảo mật để sản xuất, truyền nhận, thu thập, xử lý, lưu trữ và trao đổi thông tin số phục vụ cho việc quản lý và cung cấp dịch vụ Online Banking, do đơn vị thiết lập, quản trị, vận hành hoặc thuê bên thứ ba thiết lập, quản trị, vận hành.
3. Phần mềm ứng dụng Online Banking là phần
1. mềm ứng dụng cung cấp dịch vụ Online Banking.
4. Phần mềm ứng dụng Mobile Banking là phần
1. mềm ứng dụng Online Banking được cài đặt trên thiết bị di động.
5. Giao dịch thanh toán trực tuyến là giao dịch
1. thanh toán được thực hiện bằng phương tiện điện tử thông qua hệ thống Online Banking.
6. Khách hàng là các tổ chức, cá nhân sử dụng
1. dịch vụ Online Banking.
7. Phương thức xử lý xuyên
1. suốt (Straight-Through Processing) là phương thức trao đổi thông tin, dữ liệu, tài liệu hai chiều tự động, thông qua kết nối an toàn giữa hệ thống thông tin của khách hàng với hệ thống Online Banking.
8. Xác nhận giao dịch điện tử
1. (sau đây gọi là xác nhận giao dịch) là hình thức xác nhận bằng phương tiện điện tử để thể hiện sự chấp thuận của khách hàng đối với các thông điệp dữ liệu trong giao dịch điện tử.
9. Mã hóa điểm đầu đến điểm cuối (end to end
1. encryption) là cơ chế mã hóa an toàn thông tin ở điểm đầu trước khi gửi đi và chỉ được giải mã sau khi nhận được tại điểm cuối trong quá trình trao đổi thông tin giữa các ứng dụng, các thiết bị trong hệ thống nhằm hạn chế rủi ro bị lộ, lọt thông tin trên đường truyền.
10. Hệ quản trị cơ sở dữ liệu là phần mềm được
1. thiết kế để quản lý, lưu trữ, truy xuất và thực thi các truy vấn dữ liệu trong cơ sở dữ liệu.

## Điều 3. Nguyên tắc chung về bảo
1. đảm an toàn, bảo mật hệ thống thông tin cho việc cung cấp dịch vụ Online Banking
1. Hệ thống Online Banking phải tuân thủ quy định về
1. bảo đảm an toàn hệ thống thông tin cấp độ 3 trở lên theo quy định của pháp luật về bảo đảm an toàn hệ thống thông tin theo cấp độ, đối với hệ thống thông tin cung cấp dịch vụ chuyển mạch tài chính, dịch vụ bù trừ điện tử phải tuân thủ quy định về bảo đảm an toàn hệ thống thông tin cấp độ 4 trở lên; tuân thủ tiêu chuẩn TCVN 11930:2017 (tiêu chuẩn Công nghệ thông tin - Các kỹ thuật an toàn - Yêu cầu cơ bản về an toàn hệ thống thông tin theo cấp độ) và quy định của Ngân hàng Nhà nước về an toàn hệ thống thông tin trong hoạt động ngân hàng.
2. Bảo đảm tính bí mật, tính toàn vẹn của thông tin
1. khách hàng; bảo đảm tính sẵn sàng của hệ thống Online Banking để cung cấp dịch vụ một cách liên tục.
3. Các giao dịch của khách hàng được phân loại và
   - a) Áp dụng tối thiểu một trong
   - b) Áp dụng tối thiểu một hoặc kết hợp các hình thức
   - c) Đối với giao dịch gồm nhiều bước, phải thực hiện
4. Thực hiện kiểm tra, đánh giá an toàn, bảo mật hệ
1. thống Online Banking định kỳ hàng năm.
5. Thường xuyên nhận dạng rủi ro, nguy cơ gây ra rủi
1. ro và xác định nguyên nhân gây ra rủi ro, kịp thời có biện pháp phòng ngừa, kiểm soát và xử lý rủi ro trong cung cấp dịch vụ Online Banking.
6. Các trang thiết bị hạ tầng kỹ thuật công nghệ
1. thông tin cung cấp dịch vụ Online Banking phải có bản quyền, nguồn gốc, xuất xứ rõ ràng. Với các trang thiết bị sắp hết vòng đời sản phẩm và sẽ không được nhà sản xuất tiếp tục hỗ trợ, đơn vị phải có kế hoạch nâng cấp, thay thế theo thông báo của nhà sản xuất, bảo đảm các trang thiết bị hạ tầng có khả năng cài đặt phiên bản phần mềm mới. Trong thời gian chưa nâng cấp, thay thế, đơn vị phải có biện pháp tăng cường bảo đảm an toàn, bảo mật hệ thống Online Banking.
7. Đối với các hệ thống cung cấp dịch vụ cổng thanh
1. toán điện tử, dịch vụ hỗ trợ thu hộ, chi hộ, không phải tuân thủ các quy định tại khoản 7, khoản 9, khoản 10 Điều 7 và Mục 2 Chương II Thông tư này.
8. Hệ thống Online Banking chỉ được hoạt động cung
1. cấp dịch vụ cho khách hàng khi bảo đảm an toàn, bảo mật theo quy định của Thông tư này và các quy định của pháp luật liên quan. CÁC QUY ĐỊNH CỤ THỂ THỐNG ONLINE BANKING

## Điều 4. Hệ thống mạng, truyền
1. thông và an toàn, bảo mật Đơn vị phải thiết lập hệ thống mạng, truyền thông và an toàn, bảo mật đạt yêu cầu tối thiểu sau:
1. Có các giải pháp an toàn, bảo mật tối thiểu gồm:
   - a) Tường lửa ứng dụng hoặc giải pháp bảo vệ có tính
   - b) Tường lửa cơ sở dữ liệu hoặc giải pháp bảo vệ có
   - c) Giải pháp phòng, chống tấn công từ chối dịch vụ
   - d) Hệ thống quản lý và phân tích sự kiện an toàn
2. Thông tin khách hàng (thông tin nhận biết khách
1. hàng, thông tin giao dịch của khách hàng) không được lưu trữ tại phân vùng kết nối Internet và phân vùng trung gian giữa mạng nội bộ và mạng Internet (phân vùng DMZ).
3. Thiết lập chính sách hạn chế tối đa các dịch vụ,
1. cổng kết nối vào hệ thống Online Banking.
4. Kết nối từ bên ngoài mạng nội bộ vào hệ thống
   - a) Phải được cấp có thẩm quyền phê duyệt sau khi
   - b) Phải có phương án quản lý truy cập, quản trị hệ
   - c) Thiết bị kết nối phải được cài đặt các phần mềm
   - d) Phải áp dụng tối thiểu hai trong các hình thức
   - đ) Sử dụng giao thức truyền thông được mã hóa an
5. Đường truyền kết nối mạng cung cấp dịch vụ phải
1. bảo đảm tính sẵn sàng cao và khả năng cung cấp dịch vụ liên tục.

## Điều 5. Hệ thống máy chủ và phần
1. mềm hệ thống
1. Yêu cầu đối với máy chủ:
   - a) Hiệu năng sử dụng tài nguyên máy chủ bao gồm: bộ
   - b) Hệ thống Online Banking phải có máy chủ dự phòng
   - c) Tách biệt về lô-gíc hoặc vật lý với các máy chủ
   - d) Phải được kiểm tra, nâng cao mức độ an toàn, bảo
2. Đơn vị phải lập danh mục các phần mềm được phép
1. cài đặt trên máy chủ. Định kỳ tối thiểu 06 tháng một lần cập nhật, kiểm tra, bảo đảm tuân thủ danh mục này.

## Điều 6. Hệ quản trị cơ sở dữ liệu
1. Hệ quản trị cơ sở dữ liệu phải có cơ chế bảo vệ
1. và phân quyền truy cập đối với các tài nguyên cơ sở dữ liệu.
2. Hệ thống Online Banking phải có cơ sở dữ liệu dự
1. phòng thảm họa, có khả năng thay thế cơ sở dữ liệu chính và bảo đảm đầy đủ, toàn vẹn dữ liệu giao dịch của khách hàng.
3. Hệ quản trị cơ sở dữ liệu phải được kiểm tra,
1. nâng cao mức độ an toàn, bảo mật (hardening) và cập nhật các bản vá lỗi thường xuyên.
4. Đơn vị phải có biện pháp giám sát, ghi nhật ký
1. truy cập cơ sở dữ liệu và các thao tác khi truy cập cơ sở dữ liệu.

## Điều 7. Phần mềm ứng dụng
1. Online Banking
1. Các yêu cầu về an toàn, bảo mật phải được xác định
1. trước khi phát triển phần mềm và tổ chức, triển khai trong quá trình phát triển (phân tích, thiết kế, xây dựng, kiểm thử), vận hành chính thức và duy trì hoạt động phần mềm. Các hồ sơ, tài liệu về an toàn, bảo mật của phần mềm phải được hệ thống hóa, lưu trữ, cập nhật đồng bộ khi hệ thống có thay đổi và kiểm soát chặt chẽ, hạn chế tiếp cận.
2. Đơn vị phải kiểm soát mã nguồn phần mềm với các
   - a) Đối với mã nguồn phần mềm do đơn vị tự phát triển:
   - b) Trường hợp mã nguồn phần mềm thuê ngoài gia công
3. Phần mềm ứng dụng Online Banking phải được kiểm
   - a) Lập và phê duyệt kế hoạch, kịch bản thử nghiệm
   - b) Phát hiện và loại trừ các lỗi, các gian lận có
   - c) Đánh giá, dò quét phát hiện
   - d) Ghi lại các lỗi và quá trình xử lý lỗi, đặc biệt
   - đ) Kiểm tra thử nghiệm các tính năng an toàn, bảo mật
4. Trước khi triển khai phần mềm ứng dụng Online
1. Banking mới, đơn vị phải đánh giá những rủi ro của quá trình triển khai đối với hoạt động nghiệp vụ, các hệ thống công nghệ thông tin liên quan và lập, triển khai các phương án hạn chế, khắc phục rủi ro.
5. Đơn vị thực hiện quản lý thay đổi phiên bản phần
   - a) Xây dựng tài liệu phân tích đánh giá tác động của
   - b) Các phiên bản phần mềm bao gồm cả mã nguồn do
   - c) Thông tin về các phiên bản (thời gian cập nhật,
   - d) Việc nâng cấp phiên bản phải căn cứ trên kết quả
6. Các chức năng bắt buộc của phần mềm ứng dụng
   - a) Toàn bộ dữ liệu khi truyền trên môi trường mạng
   - b) Bảo đảm tính toàn vẹn của dữ liệu giao dịch, mọi
   - c) Kiểm soát phiên giao dịch: hệ thống có cơ chế tự
   - d) Có chức năng che giấu đối với việc hiển thị các
   - đ) Có chức năng chống đăng nhập tự động;
   - e) Trong trường hợp tài khoản giao dịch điện tử quy
   - g) Đối với khách hàng là tổ chức,
   - h) Có chức năng thông báo việc đăng nhập lần đầu phần
7. Phần mềm ứng dụng Online Banking phải có chức
   - a) Thông tin định danh về thiết bị:
   - b) Nhật ký (log) giao dịch tối thiểu gồm: mã giao dịch,
   - c) Nhật ký (log) xác nhận giao dịch tối thiểu gồm:
8. Các yêu cầu đối với phương
   - a) Đơn vị chỉ cung cấp dịch vụ Online Banking bằng
   - b) Phần mềm ứng dụng Online
   - c) Không bắt buộc áp dụng nội dung quy định tại điểm
9. Tổ chức phát hành thẻ có cung cấp dịch vụ thanh
   - a) Cho phép hoặc không cho phép thanh toán trực tuyến;
   - b) Thiết lập hạn mức thanh toán trực tuyến sử dụng
   - c) Cho phép hoặc không cho phép thanh toán ở nước
   - d) Cho phép khách hàng đăng ký lựa chọn việc chủ động
10. Phần mềm ứng dụng Online Banking phải có chức
1. năng thông báo cho khách hàng về các giao dịch phát sinh qua tin nhắn SMS hoặc thư điện tử hoặc phần mềm ứng dụng Mobile Banking hoặc các kênh liên lạc khác do khách hàng đăng ký.

## Điều 8. Phần mềm ứng dụng
1. Mobile Banking Phần mềm ứng dụng Mobile Banking do đơn vị cung cấp phải bảo đảm tuân thủ các quy định tại Điều 7 Thông tư này và các yêu cầu sau:
1. Phải được đăng ký và quản lý tại kho ứng dụng
1. chính thức của hãng cung cấp hệ điều hành cho thiết bị di động và hướng dẫn cài đặt rõ ràng trên trang tin điện tử đơn vị để khách hàng tải và cài đặt phần mềm ứng dụng Mobile Banking. Trong trường hợp vì lý do khách quan mà phần mềm ứng dụng Mobile Banking không được đăng ký và quản lý tại kho ứng dụng chính thức của hãng cung cấp hệ điều hành cho thiết bị di động, đơn vị phải có phương thức hướng dẫn, thông báo, hỗ trợ cài đặt phần mềm ứng dụng Mobile Banking bảo đảm an toàn, bảo mật cho khách hàng và báo cáo về Ngân hàng Nhà nước (Cục Công nghệ thông tin) trước khi cung cấp dịch vụ.
2. Phải được áp dụng các biện pháp bảo vệ để hạn chế
1. dịch ngược mã nguồn.
3. Có biện pháp bảo vệ, chống
1. can thiệp vào luồng trao đổi dữ liệu trên ứng dụng Mobile Banking và giữa ứng dụng Mobile Banking với máy chủ cung cấp dịch vụ Online Banking.
4. Triển khai các giải pháp nhằm
1. phòng, chống, phát hiện các hành vi can thiệp trái phép vào ứng dụng Mobile Banking đã cài đặt trong thiết bị di động của khách hàng.
5. Không cho phép chức năng ghi
1. nhớ mã khóa bí mật truy cập.
6. Đối với khách hàng cá nhân,
   - a) Khớp đúng SMS OTP hoặc Voice OTP thông qua số điện
   - b) Khớp đúng thông tin sinh trắc học theo quy định

## Điều 9. Truy cập phần mềm ứng dụng
1. Online Banking
1. Khách hàng đăng ký sử dụng phần mềm ứng dụng
1. Online Banking phải được đơn vị nhận biết khách hàng và cấp tài khoản giao dịch điện tử. Tài khoản giao dịch điện tử gồm tên đăng nhập và tối thiểu một trong các hình thức xác nhận quy định tại khoản 1, khoản 2, khoản 3, khoản 4, khoản 5, khoản 6, khoản 7, khoản 8, khoản 9 Điều 11 Thông tư này.
2. Khách hàng truy cập phần mềm ứng dụng Online
1. Banking bằng tài khoản giao dịch điện tử do đơn vị cấp hoặc truy cập bằng hình thức đăng nhập một lần (Single Sign On) thông qua tài khoản giao dịch điện tử của hệ thống thông tin khác đã được đơn vị tích hợp và theo đăng ký của khách hàng.

## Điều 10. Xác nhận giao dịch
1. Đối với giao dịch thanh toán trực tuyến:
   - a) Đối với giao dịch thanh
   - b) Đối với giao dịch thanh toán thực hiện bằng
   - c) Đối với các giao dịch thanh toán thẻ trực tuyến
   - d) Đối với các giao dịch mà
   - đ) Đối với các giao dịch
2. Đối với giao dịch đăng ký tự
1. động trích Nợ tài khoản thanh toán, tự động trích Nợ ví điện tử, tự động thanh toán từ thẻ của khách hàng, đơn vị áp dụng tối thiểu một trong các hình thức xác nhận quy định tại khoản 3, khoản 4, khoản 5, khoản 7, khoản 8, khoản 9 Điều 11 Thông tư này.
3. Đối với các giao dịch khác, ngoài giao dịch quy
1. định tại khoản 1, khoản 2 Điều này, trên cơ sở đánh giá rủi ro và tuân thủ quy định của pháp luật có liên quan, đơn vị lựa chọn hình thức xác nhận phù hợp theo quy định tại Điều 11 Thông tư này để cung cấp cho khách hàng đăng ký sử dụng và chịu trách nhiệm với việc lựa chọn này.
4. Trường hợp khách hàng là người khuyết tật, đơn vị
1. căn cứ điều kiện, khả năng cung ứng của đơn vị mình để cung cấp và hướng dẫn khách hàng là người khuyết tật lựa chọn hình thức xác nhận phù hợp, không bắt buộc áp dụng quy định tại khoản 1, khoản 2, khoản 3 Điều này, nhưng phải bảo đảm kiểm tra, xác nhận được sự chấp thuận của khách hàng khi thực hiện giao dịch theo quy định của pháp luật về giao dịch điện tử và Thông tư này.

## Điều 11. Các hình thức xác nhận
1. Hình thức xác nhận bằng mã khóa bí mật
   - a) Mã khóa bí mật có độ dài tối thiểu 08 ký tự và cấu
   - b) Thời gian hiệu lực của mã khóa bí mật tối đa 12
2. Hình thức xác nhận bằng mã PIN (Personal
   - a) Mã PIN có độ dài tối thiểu 06 ký tự;
   - b) Thời gian hiệu lực của mã PIN tối đa 12 tháng, đối
3. Hình thức xác nhận bằng mã khóa bí mật dùng một
   - a) SMS OTP là hình thức xác nhận thông qua
   - b) Voice OTP là hình thức xác nhận thông qua
   - c) Email OTP là hình thức xác nhận thông qua
   - d) Thẻ ma trận OTP là hình thức xác nhận
   - đ) Soft OTP là hình thức xác nhận thông qua
   - e) Token OTP là hình thức xác nhận thông qua
4. Hình thức xác nhận hai kênh là hình thức
1. xác nhận khi khách hàng thực hiện giao dịch, hệ thống Online Banking sẽ gửi thông tin yêu cầu xác nhận giao dịch đến thiết bị di động của khách hàng qua cuộc gọi thoại hoặc cuộc gọi thông qua dịch vụ viễn thông cơ bản trên Internet hoặc qua mã tin nhắn nhanh USSD (Unstructured Supplementary Service Data) hoặc qua phần mềm chuyên dụng, khách hàng phản hồi trực tiếp qua kênh đã kết nối để xác nhận hoặc không xác nhận thực hiện giao dịch. Yêu cầu xác nhận của hình thức xác nhận hai kênh có hiệu lực tối đa 05 phút.
5. Hình thức xác nhận khớp
   - a) Trường hợp áp dụng hình thức khớp đúng thông tin
   - b) Trường hợp áp dụng các hình thức khớp đúng thông
   - c) Giải pháp phát hiện tấn
   - d) Trường hợp khách hàng xác nhận bằng hình thức khớp
   - đ) Thời gian thực hiện khớp đúng thông tin sinh trắc
6. Hình thức xác nhận khớp đúng thông tin sinh
   - a) Chỉ cho phép kích hoạt sử dụng sau khi có sự đồng
   - b) Thời gian thực hiện khớp đúng thông tin sinh trắc
7. Hình thức xác nhận FIDO
   - a) Khóa bí mật được lưu giữ an toàn trên thiết bị của
   - b) Khóa công khai được lưu trữ an toàn tại đơn vị
   - c) Giải pháp do đơn vị tự triển
8. Hình thức xác nhận bằng chữ
1. ký điện tử theo quy định của pháp luật về chữ ký điện tử (không bao gồm chữ ký điện tử an toàn quy định tại khoản 9 Điều này).
9. Hình thức xác nhận bằng chữ
1. ký điện tử an toàn là hình thức xác nhận bằng chữ ký điện tử, trong đó chữ ký điện tử là chữ ký điện tử chuyên dùng bảo đảm an toàn hoặc chữ ký số hoặc chữ ký điện tử nước ngoài được công nhận tại Việt Nam theo quy định của pháp luật về chữ ký điện tử.
10. Hình thức xác nhận trên cơ sở đánh giá rủi ro đối
1. với giao dịch thanh toán thẻ trực tuyến theo tiêu chuẩn EMV 3-D Secure (sau đây gọi tắt là hình thức xác nhận EMV 3DS). Hình thức xác nhận EMV 3DS phải đáp ứng yêu cầu: Tổ chức phát hành thẻ, tổ chức thanh toán thẻ và đơn vị chấp nhận thẻ phải triển khai tiêu chuẩn EMV 3-D Secure.
11. Hình thức xác nhận thông qua các thao tác thể
   - a) Các thao tác xác nhận phải được lưu trữ nhật ký
   - b) Khách hàng là tổ chức và đã thực hiện đăng nhập

## Điều 12. Quản lý nhân sự quản
1. trị, vận hành hệ thống Online Banking
1. Đơn vị phải phân công nhân sự giám sát, theo dõi
1. hoạt động của hệ thống Online Banking, phát hiện và xử lý các sự cố kỹ thuật, các cuộc tấn công mạng.
2. Đơn vị phải phân công nhân sự tiếp nhận thông
1. tin, hỗ trợ khách hàng, kịp thời liên lạc với khách hàng khi phát hiện các giao dịch bất thường.
3. Nhân sự quản trị, giám sát và vận hành hệ thống
1. Online Banking phải tham gia các khóa đào tạo cập nhật kiến thức an toàn, bảo mật hằng năm.
4. Việc cấp phát, phân quyền tài khoản quản trị hệ
1. thống Online Banking phải được theo dõi, giám sát bởi bộ phận độc lập với bộ phận cấp phát tài khoản.

## Điều 13. Quản lý hoạt động của
1. môi trường vận hành hệ thống Online Banking
1. Đơn vị không cài đặt, lưu trữ phần mềm phát triển
1. ứng dụng, mã nguồn trên môi trường vận hành.
2. Hoạt động quản trị, giám sát và vận hành phải
   - a) Máy tính của nhân sự quản trị, giám sát và vận
   - b) Việc kết nối quản trị, giám sát và vận hành hệ
   - c) Việc sử dụng tài khoản có quyền quản trị phải được
   - d) Phải có biện pháp giám sát việc sử dụng tài khoản
3. Đơn vị phải thiết lập chính sách đối với các máy
1. tính thực hiện quản trị, giám sát và vận hành hệ thống Online Banking chỉ được phép kết nối đến hệ thống Online Banking hoặc các hệ thống thông tin khác của đơn vị để phục vụ quản trị, giám sát và vận hành.

## Điều 14. Quản lý lỗ hổng, điểm
1. yếu về mặt kỹ thuật Đơn vị phải thực hiện quản lý các lỗ hổng, điểm yếu của hệ thống Online Banking với các nội dung cơ bản sau:
1. Có biện pháp phòng, chống, dò tìm phát hiện các
1. thay đổi trái phép đối với phần mềm ứng dụng Online Banking.
2. Thiết lập cơ chế phát hiện, phòng chống xâm nhập,
1. tấn công mạng vào hệ thống Online Banking.
3. Phối hợp với các đơn vị quản lý nhà nước, các đối
1. tác công nghệ thông tin kịp thời nắm bắt các sự cố, tình huống mất an toàn, bảo mật thông tin để có biện pháp ngăn chặn kịp thời.
4. Cập nhật thông tin các lỗ hổng bảo mật được công
1. bố có liên quan đến phần mềm hệ thống, hệ quản trị cơ sở dữ liệu và phần mềm ứng dụng theo thông tin từ Hệ thống tính điểm lỗ hổng phổ biến (Common Vulnerability Scoring System version 4 - CVSS v4 hoặc tương đương).
5. Thực hiện dò quét lỗ hổng, điểm yếu của hệ thống
1. Online Banking tối thiểu mỗi năm một lần hoặc khi tiếp nhận được những thông tin liên quan đến lỗ hổng, điểm yếu mới. Đối với thành phần hệ thống kết nối trực tiếp với Internet thực hiện dò quét lỗ hổng, điểm yếu tối thiểu 03 tháng một lần. Đánh giá mức độ tác động, rủi ro của từng lỗ hổng, điểm yếu về mặt kỹ thuật được phát hiện của hệ thống và đưa ra phương án, kế hoạch xử lý.
6. Thực hiện triển khai cập nhật các bản vá bảo mật
   - a) Đối với lỗ hổng bảo mật được đánh giá ở mức
   - b) Đối với lỗ hổng bảo mật được đánh giá ở mức cao:
   - c) Đối với lỗ hổng bảo mật được đánh giá ở mức

## Điều 15. Hệ thống giám sát,
1. theo dõi hoạt động của hệ thống Online Banking
1. Đơn vị phải thiết lập hệ thống giám sát, theo
1. dõi hoạt động của hệ thống Online Banking. Hệ thống giám sát, theo dõi hoạt động của hệ thống Online Banking phải thu thập đầy đủ nhật ký (log) của các thành phần thuộc hệ thống Online Banking để phát hiện, điều tra các sự kiện bất thường hoặc các hành vi tấn công mạng.
2. Đơn vị phải xây dựng các tiêu chí và phần mềm để
1. cảnh báo các giao dịch bất thường dựa vào thời gian, vị trí địa lý, tần suất giao dịch, số tiền giao dịch (nếu có), số lần đăng nhập sai quá quy định và các dấu hiệu bất thường khác.

## Điều 16. Bảo đảm hoạt động
1. liên tục Đơn vị phải xây dựng hệ thống dự phòng thảm hoạ, quy trình, kịch bản bảo đảm hoạt động liên tục cho hệ thống Online Banking theo quy định của Ngân hàng Nhà nước về bảo đảm an toàn, bảo mật hệ thống công nghệ thông tin trong hoạt động ngân hàng. Ngoài ra, đơn vị phải thực hiện:
1. Phân tích, xác định các tình huống có thể gây mất
1. an toàn thông tin và gián đoạn hoạt động của hệ thống Online Banking. Xác định, đánh giá mức độ rủi ro, khả năng có thể xảy ra đối với từng tình huống tối thiểu 06 tháng một lần. Lập danh sách các tình huống có mức độ rủi ro, khả năng có thể xảy ra theo các cấp độ cao, trung bình, chấp nhận được và thấp.
2. Xây dựng phương án bao gồm quy trình, kịch bản xử
1. lý khắc phục các tình huống có mức độ rủi ro, khả năng có thể xảy ra ở cấp độ cao và trung bình theo quy định tại khoản 1 Điều này. Xác định thời gian dừng hoạt động tối đa để phục hồi hệ thống, phục hồi dữ liệu cho phương án xử lý đối với từng tình huống. Tổ chức phổ biến phương án xử lý đến các nhân sự có liên quan để hiểu rõ nhiệm vụ, công việc cần phải thực hiện khi xử lý.
3. Bố trí nguồn nhân lực, tài chính và các phương
1. tiện kỹ thuật để tổ chức diễn tập phương án xử lý với các tình huống có mức độ rủi ro, khả năng có thể xảy ra ở cấp độ cao theo định kỳ tối thiểu 01 năm một lần.
4. Lập kế hoạch và tiến hành diễn tập các biện pháp
1. bảo đảm hoạt động kinh doanh liên tục, lưu giữ các hồ sơ có liên quan và tổ chức đánh giá kết quả diễn tập. KHÁCH HÀNG

## Điều 17. Thông tin về dịch vụ
1. Online Banking
1. Đơn vị phải công bố thông tin về dịch vụ Online
   - a) Cách thức cung cấp dịch vụ, cách thức truy cập dịch
   - b) Hạn mức giao dịch (nếu có) và các hình thức xác
   - c) Các trang thiết bị cần thiết để sử dụng dịch vụ,
   - d) Các rủi ro liên quan đến việc sử dụng dịch vụ
2. Đơn vị phải thông tin cho khách hàng về các điều
   - a) Quyền lợi và nghĩa vụ của khách hàng sử dụng dịch
   - b) Các loại dữ liệu của khách hàng mà đơn vị thu thập,
   - c) Cam kết khả năng bảo đảm hoạt động liên tục của
   - d) Các nội dung khác của đơn vị đối với dịch vụ
3. Đơn vị không gửi tin nhắn
1. SMS, thư điện tử cho khách hàng có nội dung chứa đường dẫn liên kết (Hyperlink) truy cập các trang tin điện tử, trừ trường hợp theo yêu cầu của khách hàng.

## Điều 18. Hướng dẫn khách hàng
1. sử dụng dịch vụ Online Banking
1. Đơn vị phải xây dựng quy trình, tài liệu hướng dẫn
1. cài đặt, sử dụng các phần mềm, ứng dụng, thiết bị thực hiện các giao dịch điện tử và cung cấp, hướng dẫn khách hàng sử dụng các quy trình, tài liệu này.
2. Đơn vị phải hướng dẫn khách hàng thực hiện các
   - a) Bảo vệ bí mật mã khóa bí mật, mã PIN, OTP và
   - b) Nguyên tắc thiết lập mã khóa bí mật, mã PIN và
   - c) Không nên sử dụng máy tính công cộng để truy cập,
   - d) Không lưu lại tên đăng nhập và mã khóa bí mật,
   - đ) Thoát khỏi phần mềm ứng dụng Online Banking khi
   - e) Nhận dạng và hành động xử lý một số tình huống lừa
   - g) Cài đặt đầy đủ các bản vá lỗ hổng bảo mật của hệ
   - h) Lựa chọn các hình thức xác nhận giao dịch có mức
   - i) Cảnh báo các rủi ro liên quan đến việc sử dụng dịch
   - k) Không sử dụng các thiết bị di động đã bị phá
   - l) Không cài đặt các phần mềm lạ, phần mềm không có
   - m) Thông báo kịp thời cho đơn vị khi phát hiện các
   - n) Thông báo ngay cho đơn vị các trường hợp: mất,
3. Đơn vị phải cung cấp cho khách hàng thông tin về
1. đầu mối tiếp nhận thông tin, số điện thoại đường dây nóng và chỉ dẫn cho khách hàng quy trình, cách thức phối hợp xử lý các lỗi và sự cố trong quá trình sử dụng dịch vụ Online Banking.
4. Đơn vị phải giải thích cho khách hàng về những
1. trường hợp cụ thể đơn vị sẽ liên lạc với khách hàng, cách thức, phương tiện liên lạc trong quá trình khách hàng sử dụng dịch vụ Online Banking.

## Điều 19. Bảo mật thông tin
1. khách hàng Đơn vị phải áp dụng các biện pháp bảo đảm an toàn, bảo mật dữ liệu khách hàng, tối thiểu bao gồm:
1. Dữ liệu của khách hàng phải được bảo đảm an
1. toàn, bảo mật theo quy định của pháp luật.
2. Thông tin sử dụng để xác nhận giao dịch của khách
1. hàng bao gồm mã khóa bí mật, mã PIN, thông tin sinh trắc học khi lưu trữ phải áp dụng các biện pháp mã hóa hoặc che dấu để bảo đảm tính bí mật.
3. Thiết lập quyền truy cập đúng chức năng, nhiệm vụ
1. cho nhân sự thực hiện nhiệm vụ truy cập dữ liệu khách hàng; có biện pháp giám sát mỗi lần truy cập.
4. Có biện pháp quản lý truy cập, tiếp cận các thiết
1. bị, phương tiện lưu trữ dữ liệu của khách hàng để phòng chống nguy cơ lộ, lọt dữ liệu.
5. Thông báo cho khách hàng khi xảy ra sự cố làm lộ,
1. lọt dữ liệu của khách hàng và báo cáo kịp thời về Ngân hàng Nhà nước Việt Nam (Cục Công nghệ thông tin). ĐIỀU KHOẢN THI HÀNH

## Điều 20. Chế độ báo cáo
1. Các đơn vị cung cấp dịch vụ Online Banking có trách nhiệm gửi báo cáo bằng văn bản về Ngân hàng Nhà nước Việt Nam (Cục Công nghệ thông tin) như sau:
1. Báo cáo cung cấp dịch vụ Online Banking:
   - a) Thời hạn gửi báo cáo: Tối thiểu 10 ngày làm việc
   - b) Nội dung báo cáo:
2. Báo cáo đột xuất theo yêu cầu của Ngân hàng Nhà
1. nước.

## Điều 21. Trách nhiệm của các
1. đơn vị thuộc Ngân hàng Nhà nước
1. Cục Công nghệ thông tin có trách nhiệm theo dõi,
1. kiểm tra và phối hợp với các đơn vị liên quan để xử lý những vướng mắc phát sinh trong quá trình thực hiện Thông tư này.
2. Cơ quan Thanh tra, giám sát ngân hàng có trách
1. nhiệm thanh tra, giám sát việc thi hành Thông tư này và xử lý các trường hợp vi phạm theo quy định của pháp luật.
3. Ngân hàng Nhà nước chi nhánh tỉnh, thành phố có
1. trách nhiệm thanh tra, giám sát việc thực hiện Thông tư này tại các tổ chức cung ứng dịch vụ trung gian thanh toán trên địa bàn (trừ Công ty Cổ phần Thanh toán Quốc gia Việt Nam) và xử lý các trường hợp vi phạm theo quy định của pháp luật.

## Điều 22. Hiệu lực thi hành
1. Thông tư này có hiệu lực thi hành kể từ ngày 01
1. tháng 01 năm 2025, trừ trường hợp quy định tại khoản 2, khoản 3, khoản 4 Điều này.
2. Điểm b khoản 1 Điều 4, điểm d
1. khoản 9 Điều 7, khoản 3 và khoản 4 Điều 8 có hiệu lực thi hành kể từ ngày 01 tháng 07 năm 2025.
3. Điểm b khoản 1 Điều 10 có hiệu
1. lực thi hành kể từ ngày 01 tháng 01 năm 2026.
4. Điểm c khoản 5 Điều 11, điểm c
1. khoản 7 Điều 11, điểm b (iv) khoản 1 Điều 20 có hiệu lực thi hành kể từ ngày 01 tháng 07 năm 2026.
5. Các văn bản sau đây hết hiệu lực kể từ ngày
   - a) Thông tư số 35/2016/TT-NHNN
   - b) Thông tư số 35/2018/TT-NHNN
6. Bãi bỏ Điều
1. 25 của Thông tư số 09/2020/TT-NHNN ngày 21 tháng 10 năm 2020 của Thống đốc Ngân hàng Nhà nước Việt Nam quy định về an toàn hệ thống thông tin trong hoạt động ngân hàng.

## Điều 23. Quy định chuyển tiếp
1. Các giao dịch đăng ký tự động trích Nợ tài khoản
1. thanh toán, tự động trích Nợ ví điện tử, tự động thanh toán từ thẻ của khách hàng được thực hiện trước ngày Thông tư này có hiệu lực thi hành được tiếp tục thực hiện đến hết thời hạn của thỏa thuận đã giao kết; trường hợp thỏa thuận không xác định thời hạn thì được tiếp tục thực hiện đến hết ngày 31 tháng 12 năm 2026. Việc sửa đổi, bổ sung, gia hạn thỏa thuận phải tuân thủ theo quy định tại khoản 2 Điều 10 Thông tư này.
2. Các mã khóa bí mật, mã PIN đang được sử dụng trước
1. ngày Thông tư này có hiệu lực thi hành thì được tiếp tục sử dụng cho đến khi khách hàng thay đổi hoặc đến hết thời gian hiệu lực của mã khóa bí mật, mã PIN. Kể từ ngày Thông tư này có hiệu lực, các mã khóa bí mật, mã PIN khi thay đổi phải tuân thủ quy định tại khoản 1, khoản 2 Điều 11 Thông tư này.

## Điều 24. Tổ chức thực hiện
1. Chánh Văn phòng, Cục trưởng Cục Công nghệ thông tin và Thủ trưởng các đơn vị thuộc Ngân hàng Nhà nước Việt Nam, Chủ tịch Hội đồng quản trị, Chủ tịch Hội đồng thành viên, Tổng giám đốc (Giám đốc) các tổ chức tín dụng, chi nhánh ngân hàng nước ngoài, các tổ chức cung ứng dịch vụ trung gian thanh toán, công ty thông tin tín dụng chịu trách nhiệm tổ chức thực hiện Thông tư này./. Nơi nhận: - Như Điều 24; - Ban Lãnh đạo NHNN; - Văn phòng Chính phủ; - Bộ Tư pháp (để kiểm tra); - Công báo; - Lưu VP, PC, CNTT. KT. THỐNG ĐỐC PHÓ THỐNG ĐỐC Phạm Tiến Dũng PHỤ LỤC 01 PHÂN LOẠI GIAO DỊCH THANH TOÁN TRỰC TUYẾN (kèm theo Thông tư số 50/2024/TT-NHNN ngày 31 tháng 10 năm 2024 của Thống đốc Ngân hàng Nhà nước) Loại hình giao dịch Giao dịch loại Giao dịch loại Giao dịch loại Giao dịch loại Khách hàng cá nhân Nhóm I.1: - Chuyển tiền giữa các tài khoản thanh toán, thẻ ghi nợ, thẻ trả trước định danh (sau đây gọi chung là thẻ) của một khách hàng trong một tổ chức cung ứng dịch vụ thanh toán. - Chuyển tiền giữa các ví điện tử của một khách hàng trong một tổ chức cung ứng dịch vụ trung gian thanh toán. Tất cả các giao dịch. Nhóm I.2: - Các giao dịch thanh toán hàng hóa, dịch vụ hợp pháp được tổ chức cung ứng dịch vụ thanh toán, trung gian thanh toán cung cấp hoặc tại các đơn vị chấp nhận thanh toán do các tổ chức cung ứng dịch vụ thanh toán, trung gian thanh toán chịu trách nhiệm lựa chọn, thẩm định, giám sát và quản lý. Giao dịch thỏa mãn điều kiện: G + T ≤ 5 triệu VND. Giao dịch thỏa mãn các điều kiện: (i) G + T > 5 triệu VND. (ii) G + T ≤ 100 triệu VND. Giao dịch thỏa mãn các điều kiện: (i) G + T > 100 triệu VND. (ii) G + T ≤ 1,5 tỷ VND. Giao dịch thỏa mãn điều kiện: G + T > 1,5 tỷ VND. Nhóm I.3: - Chuyển tiền giữa các tài khoản thanh toán, thẻ, ví điện tử của các chủ tài khoản, chủ thẻ, chủ ví điện tử khác nhau. - Chuyển tiền giữa các tài khoản, thẻ, ví điện tử mở tại các tổ chức cung ứng dịch vụ thanh toán, tổ chức phát hành thẻ, tổ chức cung ứng dịch vụ trung gian thanh toán khác nhau. - Nạp tiền vào Ví điện tử1. - Rút tiền ra khỏi Ví điện tử. Giao dịch nạp, rút tiền giữa Ví điện tử và tài khoản đồng Việt Nam của chủ ví điện tử tại ngân hàng liên kết theo quy định của pháp luật thỏa mãn các điều kiện: (i) G ≤ 10 triệu VND. (ii) G + Tksth ≤ 20 triệu VND. Giao dịch (ngoại trừ giao dịch nạp, rút tiền giữa Ví điện tử và tài khoản đồng Việt Nam của chủ ví điện tử tại ngân hàng liên kết theo quy định của pháp luật) thỏa mãn các điều kiện: (i) G ≤ 10 triệu VND. (ii) G + Tksth ≤ 20 triệu VND. Giao dịch thỏa mãn một trong các trường hợp sau:
1. Trường hợp 1: Giao dịch thỏa mãn các điều kiện:
1. (i) G ≤ 10 triệu VNĐ. (ii) G + Tksth > 20 triệu VND. (iii) G + T ≤ 1,5 tỷ VND.
2. Trường hợp 2: Giao dịch thỏa mãn các điều kiện:
1. (i) G > 10 triệu VND. (ii) G ≤ 500 triệu VND. (iii) G + T ≤ 1,5 tỷ VND. Giao dịch thỏa mãn một trong các trường hợp sau:
1. Trường hợp 1: Giao dịch thỏa mãn các điều kiện:
1. (i) G ≤ 10 triệu VND. (ii) G + Tksth > 20 triệu VND. (iii) G + T > 1,5 tỷ VND.
2. Trường hợp 2: Giao dịch thỏa mãn các điều kiện:
1. (i) G > 10 triệu VND. (ii) G ≤ 500 triệu VND. (iii) G + T > 1,5 tỷ VND.
3. Trường hợp 3: Giao dịch thỏa mãn điều kiện:
1. G > 500 triệu VND. Nhóm I.4: Chuyển tiền liên ngân hàng ra nước ngoài2. Giao dịch thỏa mãn các điều kiện: (i) G ≤ 200 triệu VND. (ii) G + T ≤ 1 tỷ VND. Giao dịch thỏa mãn một trong các trường hợp sau:
1. Trường hợp 1: Giao dịch thỏa mãn các điều kiện:
1. (i) G ≤ 200 triệu VND. (ii) G + T > 1 tỷ VND.
2. Trường hợp 2: Giao dịch thỏa mãn điều kiện:
1. G > 200 triệu VND. Khách hàng tổ chức3 Nhóm II.1: Chuyển tiền giữa các tài khoản thanh toán hoặc Ví điện tử của cùng một khách hàng trong một tổ chức cung ứng dịch vụ thanh toán hoặc tổ chức cung ứng dịch vụ trung gian thanh toán. Tất cả các giao dịch. Nhóm II.2: - Chuyển tiền giữa các tài khoản thanh toán, ví điện tử của các chủ tài khoản, chủ ví điện tử khác nhau. - Chuyển tiền giữa các tài khoản, ví điện tử mở tại các tổ chức cung ứng dịch vụ thanh toán, tổ chức cung ứng dịch vụ trung gian thanh toán khác nhau. - Các giao dịch thanh toán hàng hóa, dịch vụ hợp pháp được tổ chức cung ứng dịch vụ thanh toán, trung gian thanh toán cung cấp hoặc tại các đơn vị chấp nhận thanh toán do các tổ chức cung ứng dịch vụ thanh toán, trung gian thanh toán chịu trách nhiệm lựa chọn, thẩm định, giám sát và quản lý. - Nạp tiền vào Ví điện tử1. - Rút tiền ra khỏi Ví điện tử. Giao dịch thỏa mãn các điều kiện: (i) G ≤ 1 tỷ VND. (ii) G + T ≤ 10 tỷ VND. Giao dịch thỏa mãn một trong các trường hợp sau:
1. Trường hợp 1: Giao dịch thỏa mãn các điều kiện:
1. (i) G ≤ 1 tỷ VND. (ii) G + T > 10 tỷ VND.
2. Trường hợp 2: Giao dịch thỏa mãn điều kiện:
1. G > 1 tỷ VND. Nhóm II.3: Chuyển tiền liên ngân hàng ra nước ngoài2. Giao dịch thỏa mãn các điều kiện: (i) G ≤ 500 triệu VND. (ii) G + T ≤ 5 tỷ VND. Giao dịch thỏa mãn một trong các trường hợp sau:
1. Trường hợp 1: Giao dịch thỏa mãn các điều kiện:
1. (i) G ≤ 500 triệu VNĐ. (ii) G + T > 5 tỷ VND.
2. Trường hợp 2: Giao dịch thỏa mãn điều kiện:
1. G > 500 triệu VNĐ. Ghi chú: G: Giá trị của giao dịch. Tksth: Tổng giá trị các giao dịch loại A và loại B của từng nhóm loại hình giao dịch đã thực hiện của một tài khoản thanh toán hoặc một thẻ (bao gồm cả giao dịch nạp tiền vào ví điện tử) hoặc một ví điện tử (không bao gồm giao dịch nạp tiền vào ví điện tử) của khách hàng tại một tổ chức cung ứng dịch vụ thanh toán hoặc tổ chức cung ứng dịch vụ trung gian thanh toán, không bao gồm các giao dịch chủ động trích Nợ tài khoản thanh toán, chủ động trích Nợ ví điện tử, chủ động thanh toán từ thẻ. Tksth được tính giá trị bằng 0 tại thời điểm đầu ngày hoặc ngay sau khi khách hàng có phát sinh giao dịch trong ngày sử dụng hình thức xác nhận cho giao dịch loại C hoặc loại D. T: Tổng giá trị các giao dịch của từng nhóm loại hình giao dịch đã thực hiện trong ngày (của một tài khoản thanh toán hoặc một thẻ (bao gồm cả giao dịch nạp tiền vào ví điện tử) hoặc một ví điện tử (không bao gồm giao dịch nạp tiền vào ví điện tử) của khách hàng tại một tổ chức cung ứng dịch vụ thanh toán hoặc tổ chức cung ứng dịch vụ trung gian thanh toán), không bao gồm các giao dịch chủ động trích Nợ tài khoản thanh toán, chủ động trích Nợ ví điện tử, chủ động thanh toán từ thẻ. (1) Đối với giao dịch nạp tiền vào Ví điện tử từ tài khoản đồng Việt Nam của chủ ví điện tử tại ngân hàng liên kết, việc phân loại giao dịch căn cứ theo tài khoản thanh toán liên kết với Ví điện tử. (2) Hạn mức quy đổi theo tỷ giá tại thời điểm thực hiện giao dịch. (3) Trường hợp khách hàng là hộ kinh doanh hoặc doanh nghiệp siêu nhỏ áp dụng chế độ kế toán đơn giản, việc phân loại giao dịch tương tự khách hàng cá nhân. PHỤ LỤC 02 XÁC NHẬN GIAO DỊCH THANH TOÁN TRỰC TUYẾN (ban hành kèm theo Thông tư số 50/2024/TT-NHNN ngày 31 tháng 10 năm 2024 của Thống đốc Ngân hàng Nhà nước) Giao dịch Hình thức xác nhận giao dịch thanh toán trực tuyến tối thiểu Khách hàng cá nhân Khách hàng tổ chức Giao dịch loại A - Mã khóa bí mật hoặc mã PIN (trường hợp đã xác nhận tại bước đăng nhập thì không bắt buộc phải xác nhận tại bước thực hiện giao dịch). - Mã khóa bí mật hoặc mã PIN (trường hợp đã xác nhận tại bước đăng nhập thì không bắt buộc phải xác nhận tại bước thực hiện giao dịch). Giao dịch loại B - SMS OTP hoặc Voice OTP hoặc Email OTP; - Hoặc Thẻ ma trận OTP; - Hoặc Soft OTP/ Token OTP loại cơ bản hoặc nâng cao; - Hoặc hai kênh; - Hoặc khớp đúng thông tin sinh trắc học thiết bị1; - Hoặc FIDO; - Hoặc chữ ký điện tử; - Hoặc chữ ký điện tử an toàn. - SMS OTP hoặc Voice OTP hoặc Email OTP; - Hoặc Thẻ ma trận OTP; - Hoặc khớp đúng thông tin sinh trắc học thiết bị của người đại diện hợp pháp hoặc cá nhân được người đại diện hợp pháp ủy quyền (nếu có). Giao dịch loại C - OTP gửi qua SMS/Voice hoặc Soft OTP/Token OTP loại cơ bản hoặc chữ ký điện tử, - Và kết hợp khớp đúng thông tin sinh trắc học. - Soft OTP/Token OTP loại cơ bản; - Hoặc hai kênh; - Hoặc chữ ký điện tử. Giao dịch loại D - Soft OTP/Token OTP loại nâng cao hoặc FIDO hoặc chữ ký điện tử an toàn, - Và kết hợp khớp đúng thông tin sinh trắc học. - Soft OTP/Token OTP loại nâng cao; - Hoặc FIDO; - Hoặc chữ ký điện tử an toàn. Ghi chú: - Các hình thức xác nhận quy định chi tiết tại Điều 11 Thông tư này. - Hình thức xác nhận giao dịch loại D có thể xác nhận giao dịch loại A, B, C. - Hình thức xác nhận giao dịch loại C có thể xác nhận giao dịch loại A, B. - Hình thức xác nhận giao dịch loại B có thể xác nhận giao dịch loại A. - Trường hợp khách hàng là hộ kinh doanh hoặc doanh nghiệp siêu nhỏ áp dụng chế độ kế toán đơn giản, áp dụng hình thức xác nhận giao dịch tương tự khách hàng cá nhân. Trong đó, đối với hình thức khớp đúng thông tin sinh trắc học và hình thức khớp đúng thông tin sinh trắc học thiết bị, thông tin sinh trắc học sử dụng để đối chiếu, so sánh là của người đại diện hợp pháp hoặc cá nhân được người đại diện hợp pháp ủy quyền (nếu có). (1) Trường hợp khách hàng đã đăng nhập ứng dụng Online Banking bằng khớp đúng thông tin sinh trắc học thiết bị, không áp dụng biện pháp xác nhận này khi thực hiện giao dịch trong phiên đăng nhập đó. PHỤ LỤC 03 PHÂN LOẠI GIAO DỊCH THANH TOÁN THẺ TRỰC TUYẾN (ban hành kèm theo Thông tư số 50/2024/TT-NHNN ngày 31 tháng 10 năm 2024 của Thống đốc Ngân hàng Nhà nước) Loại hình giao dịch Giao dịch loại Giao dịch loại Giao dịch loại Các giao dịch thanh toán hàng hóa, dịch vụ hợp pháp được tổ chức cung ứng dịch vụ thanh toán cung cấp hoặc tại các đơn vị chấp nhận thẻ do các tổ chức cung ứng dịch vụ thanh toán chịu trách nhiệm lựa chọn, thẩm định, giám sát và quản lý. Giao dịch thỏa mãn điều kiện: G + T ≤ 5 triệu VND. Giao dịch thỏa mãn các điều kiện: (i) G + T > 5 triệu VND. (ii) G + T ≤ 100 triệu VND. Giao dịch thỏa mãn các điều kiện: G + T > 100 triệu VND. Ghi chú: G: Giá trị của giao dịch. T: Tổng giá trị các giao dịch đã thực hiện trong ngày của thẻ đang giao dịch của khách hàng tại một tổ chức phát hành thẻ, không bao gồm các giao dịch do tổ chức phát hành thẻ chủ động thanh toán từ thẻ theo thỏa thuận với khách hàng. PHỤ LỤC 04 XÁC NHẬN GIAO DỊCH THANH TOÁN THẺ TRỰC TUYẾN (ban hành kèm theo Thông tư số 50/2024/TT-NHNN ngày 31 tháng 10 năm 2024 của Thống đốc Ngân hàng Nhà nước) Giao dịch Hình thức xác nhận giao dịch thanh toán thẻ trực tuyến tối thiểu Giao dịch loại E Mã khóa bí mật hoặc mã PIN (trường hợp đã xác nhận tại bước đăng nhập thì không bắt buộc phải xác nhận tại bước thực hiện giao dịch). Giao dịch loại F - SMS OTP hoặc Voice OTP hoặc Email OTP; - Hoặc Thẻ ma trận OTP; - Hoặc Soft OTP/ Token OTP loại cơ bản; - Hoặc khớp đúng thông tin sinh trắc học thiết bị; - Hoặc hai kênh. Giao dịch loại G - Soft OTP/Token OTP loại nâng cao; - Hoặc FIDO; - Hoặc chữ ký điện tử/ chữ ký điện tử an toàn; - Hoặc EMV 3DS. Ghi chú: - Các hình thức xác nhận quy định chi tiết tại Điều 11 Thông tư này. - Hình thức xác nhận giao dịch loại G có thể xác nhận giao dịch loại E, F. - Hình thức xác nhận giao dịch loại F có thể xác nhận giao dịch loại E. Lưu trữ Ghi chú Ý kiếnFacebook Email Bài liên quan: Hướng dẫn khách hàng sử dụng dịch vụ Online Banking Các hình thức xác nhận giao dịch thanh toán trực tuyến qua Online Banking theo Thông tư 50 năm 2024 Văn bản nổi bật tuần 47 năm 2024 Các yêu cầu trong hình thức xác nhận khớp đúng thông tin sinh trắc học của dịch vụ Online Banking Các chức năng bắt buộc của phần mềm ứng dụng Online Banking từ năm 2025 Hỏi đáp pháp luật $(document).ready(function () { $.get("https://thuvienphapluat.vn/hoi-dap-phap-luat/get-top-news-by-laws?topNum=5&listIdLaw=327954", function (data) { var json = data; if (json.length > 0) { var title = $("#tab8 > div > div span").text().trim(); var newTitle = title.replace(/[?&]/g, "-"); $(".ulnhch01").show(); for (var i = 0; i " + json[i].Title + ""); else { $(".ulnhch01").hide(); }).success(function () { Pháp Luật Thuế $(document).ready(function () { $.get("https://thuvienphapluat.vn/ma-so-thue/get-top-news-by-laws?topNum=5&listIdLaw=327954", function (data) { var json = data; if (json.length > 0) { var title = $("#tab8 > div > div span").text().trim(); var newTitle = title.replace(/[?&]/g, "-"); $(".ulnhch05").show(); for (var i = 0; i " + json[i].Title + ""); else { $(".ulnhch05").hide(); }).success(function () { Bản án liên quan $(document).ready(function () { $.get("https://thuvienphapluat.vn/banan/api/ban-an-theo-van-ban-327954", function (data) { var json = data; if (json.Data != null && json.Data != undefined && json.Data.length > 0) { $(".ahd2").attr("href", json.link); $(".ulnhch02").show(); var title = $("#tab8 > div > div span").text().trim(); ; var newTitle = title.replace(/[?&]/g, "-"); for (var i = 0; i " + json.Data[i].TieuDe + ""); else { $(".ulnhch02").hide(); }).success(function () { PHÁP LUẬT DOANH NGHIỆP $(document).ready(function () { $.get("https://thuvienphapluat.vn/phap-luat-doanh-nghiep/back-link-pldn-327954", function (data) { var json = data.models; if (json != null && json != undefined && json.length > 0) { var title = $("#tab8 > div > div span").text().trim(); var newTitle = title.replace(/[?&]/g, "-"); $(".blPLDN").show(); for (var i = 0; i " li += " " + json[i].ArticleTitle + ""; li += ""; $(".blPLDN div.ttlq ul").append(li); else { var li = "" li += "" + json[i].ArticleTitle + ""; li += ""; $(".blPLDN div.ttlq ul").append(li); }).success(function () { $(".yotubeiframe").click(function myfunction() { var p = $(this).parent(); var yw = p.attr("yw"); var yh = p.attr("yh"); var yid = p.attr("yid"); p.html(""); .yotubeiframe cursor: pointer; background-size: cover; background-position: center center; background-repeat: no-repeat; position: relative; border: 1px solid #e9edf1; .ytparent .play background: red; fill-opacity: .8; border-radius: 10%; color: #FFFFFF; font-size: 1em; height: 1.5em; width: 2em; padding: 0; position: relative; text-align: center; text-indent: 0.1em; transition: all 150ms ease-out; position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); line-height: 75px; cursor: pointer; .ytparent .play::before background: inherit; border-radius: 10%; bottom: 9%; content: ""; left: -5%; position: absolute; right: -5%; top: 9%; .ytparent .play::after border-style: solid; border-width: 1em 0 1em 1.732em; border-color: transparent transparent transparent rgba(255, 255, 255, 0.75); content: ' '; font-size: 0.5em; height: 0; margin: -1em 0 0 -0.75em; top: 50%; position: absolute; width: 0; Thông tư 50/2024/TT-NHNN quy định về an toàn, bảo mật cho việc cung cấp dịch vụ trực tuyến trong ngành Ngân hàng do Thống đốc Ngân hàng Nhà nước Việt Nam ban hành var userID = "0"; var lawid = "327954"; var _title = $("._title").text(); function NotifiLawStatus() { if (userID == "0") { opentLogin(); else { $("#NotifiLawStatus-dialog-form #cpCusID").val(userID); $("#NotifiLawStatus-dialog-form #cpLawID").val(lawid); $("#NotifiLawStatus-dialog-form #VBNotifiLawStatus").html(_title); $("#NotifiLawStatus-dialog-form").dialog("open"); function VBCoNoiDungStatus() { if (userID == "0") { opentLogin(); else { $("#NotifiLawVBCoNoiDung-dialog-form #vbcnd_cpCustID").val(userID); $("#NotifiLawVBCoNoiDung-dialog-form #vbcnd_cpLawID").val(lawid); $("#NotifiLawVBCoNoiDung-dialog-form #VBCoNoiDungStatus").html(_title); $("#NotifiLawVBCoNoiDung-dialog-form").dialog("open"); function LawNote() { if (userID == "0") { opentLogin(); else { $("#Note-dialog-form #cpCusID").val(userID); $("#Note-dialog-form #cpLawID").val(lawid); $("#Note-dialog-form #VBNotifiLawStatus").html(_title); if ($("#Note-dialog-form #fbNote").val() == "") { var params = "cpCusID=" + userID + "&cpLawID=" + lawid; $.ajax({ 'url': '/page/ajaxcontroler.aspx', 'data': params + '&action=GetLawNote', 'type': 'POST', success: function (response) { $("#Note-dialog-form #fbNote").val(response); $("#Note-dialog-form").dialog("open"); error: function (response) { else { $("#Note-dialog-form").dialog("open"); function BVLQ_VB(val) { _gaq.push(['_trackEvent', 'UserActivity', 'BVLQ_VB', val]); $(document).ready(function () { if (MemberGA != 'Anonymous') { guiders.createGuider({ attachTo: "#ctl00_Content_ThongTinVB_ChiaSe_lbtSave", buttons: [], description: "+ Lưu giữ văn bản này vào \"Văn bản của tôi\"+ Có thể quản lý trong Menu chức năng Cá nhân", id: "Guiders_Save", position: 9, width: 250, title: "VĂN BẢN CỦA TÔI", xButton: true if ($.cookies.test() && $.cookies.get("Cookie_Guiders" + MemberGA) == '1' && $.cookies.get("Cookie_Guiders_Save" + MemberGA) != '1' && window.location.pathname.indexOf("tab=") == -1) { $.cookies.set("Cookie_Guiders_Save" + MemberGA, "1", { expiresAt: new Date(2016, 1, 1) }); guiders.show('Guiders_Save'); function DeleteDoc(val) { if ($('#' + val.id).html() == "Lưu trữ") { // var params = "LawID=" + $('.smhLawID').val() + "&Type=Add"; // $.ajax({ 'url': '/page/ajaxcontroler.aspx', // 'data': params + '&action=AddOrDeleteMyDoc', // 'type': 'POST', // success: AddOrDeleteMyDoc, // error: function (response) { // } // }); $("#FavoriteFolderfrom #FavoriteLawID").val($('.smhLawID').val()); $("#FavoriteFolderfrom .Fcheckbox").each(function myfunction() { $(this).attr('checked', false); $("#FavoriteFolderfrom #fdParent").html("Chọn thư mục cha"); $("#FavoriteFolderfrom ul li label").each(function myfunction() { if ($(this).attr("parentid") == "0") { $("#FavoriteFolderfrom #fdParent").append("" + $(this).html() + ""); $(this).parent().find("> div").each(function myfunction() { var lb = $(this).find("label"); $("#FavoriteFolderfrom #fdParent").append(" " + lb.html() + ""); $("#FavoriteFolderfrom").dialog("open"); else { var params = "LawID=" + $('.smhLawID').val() + "&Type=Delete"; $.ajax({ 'url': '/page/ajaxcontroler.aspx', 'data': params + '&action=AddOrDeleteMyDoc', 'type': 'POST', success: AddOrDeleteMyDoc, error: function (response) { return false; function AddOrDeleteMyDoc(response) { if (response != "") { if (response.substr(0, 3) == "Add") { $('.TotalVanBAnCuaToi').html(parseInt($('.TotalVanBAnCuaToi').html()) + 1); $('.AddOrDeleteMyDoc').html("Xóa lưu trữ"); $("#FavoriteFolderfrom").dialog("close"); else if (response.substr(0, 3) == "Del") { $('.TotalVanBAnCuaToi').html(parseInt($('.TotalVanBAnCuaToi').html()) - 1); $("#error-dialog-form").html(response.substr(3)); $("#error-dialog-form").dialog("open"); $('.AddOrDeleteMyDoc').html("Lưu trữ"); else { $("#error-dialog-form").html(response); $("#error-dialog-form").dialog("open"); .sticky .stickyYotube { position: fixed; top: 0; margin-top: 10px; z-index: 99; .cdlq ul { margin: 0; padding: 0; margin-top: 15px; .cdlq ul li{ margin: 0; padding: 0; list-style-type:none; .cdlq ul li:first-child { font: normal 16px Arial, sans-serif; font-weight: bold; color: #555; border-bottom: 1px solid #f7721b; width: 100%; .cdlq a width: 100%; color: #066cd2; text-align: left; padding-top: 10px; font-size: 14px; .cdlq ul li:first-child a{ font-size:16px; In mục lục THE STATE BANK OF VIETNAM THE SOCIALIST REPUBLIC OF VIETNAM Independence - Freedom - Happiness No. 50/2024/TT-NHNN Hanoi, October 31, 2024 CIRCULARPROVIDING FOR SECURITY AND CONFIDENTIALITY DURING PROVISION OF ONLINE BANKING SERVICESPursuant to the Law on the State Bank of Vietnam dated June 16, 2010;Pursuant to the Law on Cyberinformation Security dated November 19, 2015;Pursuant to the Law on Cybersecurity dated June 12, 2018;Pursuant to the Law on E-Transactions dated June 22, 2023;Pursuant to the Law on Credit Institutions dated January 18, 2024;Pursuant to the Government’s Decree No. 102/2022/ND-CP dated December 12, 2022 defining the functions, tasks, powers and organizational structure of the State Bank of Vietnam;.........Hãy đăng nhập hoặc đăng ký Thành viên Pro tại đây để xem toàn bộ văn bản tiếng Anh.The Governor of the State Bank of Vietnam hereby promulgates a Circular providing for security and confidentiality during provision of online banking services.Chapter IGENERAL PROVISIONS