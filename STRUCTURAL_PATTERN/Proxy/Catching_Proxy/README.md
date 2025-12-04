Mô phỏng cấu trúc kế thừa:
- Ban đầu sẽ khởi tạo một abstract object ở file First_Object.py sau đó sẽ tạo ra một object thật thông qua Real_Object.py và Catching_Proxy sẽ đóng vai trờ tạo và lưu trữ lại object cần thiết.

Mô phỏng quá trình thực thi:
- Ban đầu client sẽ gửi một request yêu cầu khởi tạo một object thi Catching sẽ tiến hành kiểm tra nếu đã có object đó ròi thì trả cho client luôn, nếu chưa có thì mới tạo mới