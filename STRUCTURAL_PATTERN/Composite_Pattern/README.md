Mô phỏng quá trình thực thi:
- Ban đầu sẽ tạo ra một abstract class IProduct để  định nghĩa các phương thức ban đầu cho Product.
- Sau đó Product sẽ kế thừa lại IProduct và overwrite lại các hàm cần thiết.
- Class Invoice (hoá đơn) cũng sẽ kế thừa lại từ Product để lưu trữ tiền của các sản phẩm và hiển thị cho client để client xem bảng giá.