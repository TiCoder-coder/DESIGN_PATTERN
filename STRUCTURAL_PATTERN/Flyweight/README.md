Mô phỏng cấu trúc kế thừa:
- Ban đầu class IFlyweight sẽ khởi tạo ban đầu và class Flyweight sẽ kế thừa lại IFlyweight để tạo ra các thuộc tính cần thiết.
- Sau đó class FlyweightFactory sẽ khởi tạo một danh sách dùng để lưu trữ các kí tự không trùng lặp lúc client gửi và được xử lý thông qua Context.

Mô phỏng quá trình thực thi:
- Lúc client gửi một chuỗi kí tự thì class Context sẽ nhận chuỗi đó và đưa cho class Flyweight_factory, class này sẽ lưu trữ lại các kĩ tự trong chuỗi (không trùng lặp) ==> Tiết kiệm bộ nhớ.