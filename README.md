DESGIN PATTERN

![Picture](https://gpcoder.com/wp-content/uploads/2018/08/design-patterns.jpg)

Design pattern dùng để cho code tuần thủ nguyên tắc SOLID

Design pattern đươc chia làm 3 nhóm chính:
Creational: (gồm có 5 nhóm nhỏ: Factory Mothod, Abstract Factory, Builder, Prototype, Singleton).
Structural: (gồm có 7 nhóm: Adapter, Bridge, Composite, Decorator, Facede, Flyweight, Proxy).
Behaviour: (gồm 11 nhóm: Chain of respository, command, iterator, mediator, memento, observer, state, strategy, template method, visitor, interpreter).

I.CREATETIONAL DESIGN PATTERN: giải quyết vấn đề làm thế nào để tạo ra một object mới
1. Factory method pattern:
- Được sử dụng để tạo ra một object nhưng không biết rõ tạo ra object đó thuộc type nào và cần một điều kiện nào đó thì lúc đó sử dụng Factory method.
- Tạo một object không phụ thuộc vào class con (tạo các object random - không cần biết nó tạo ra gì).

2. Abstract factory method:
- Thay vì tạo ra một factory như factory method thì abstract factory nó sẽ tạo ra một bộ object đông bộ nhau.
- Thay đổi object dễ dàng mà không cần sửa code.
3. Builder pattern:
- Giúp chia nhỏ các constructer và có thể khởi tạo một object theo nhiều hướng khác nhau.
-Tách logic xây dựng product thành nhiều bước nhỏ.

4.Prototype pattern: 
- Dùng để giải quyết ván đề tạo object mới nhưng chỉ khác object cũ chỉ vài thuộc tính, lúc đó ta dùng prototype pattern code sẽ đẹp và ngọn nhẹ hơn.

5.Singleton: 
- Đảm bảo rằng 1 class chỉ tạo ra duy nhất một instance cho toàn bộ chương trình và đồng thời cung cấp một điểm truy cập toàn cục đến instance đó.
- Dùng khi Logger, kết nối database,…

II. STRUCTERAL PATTERN:
1. Adapter pattern: 
- Dùng để chuyển đổi một inference của một class nào đó theo interface mà client mong muốn, giúp cho các class dù cho có khác code (không tương thích) vẫn làm việc được với nhau.
2. Bridge pattern:
Dùng để chia một class làm 2 phần chính là abstraction và inplemetation để có phát triển một cách độc lập lẫn nhau. 
	- Abstraction: thể hiện cho giao diện interface hoặc cái mà client sử dụng -- nó không cần quan tâm đến bên trong có gì. Đóng vai trò trung gian giữa client và hệ thống.
	- Implementation: Đại diện cho các class và interface bao gồm việc triển khai chi tiết cho từng chức năng, có thể có nhiều kiểu implementation cho abstraction.

3. Composite pattern:
	Dùng để xử lí một tập hợp các object theo cấu trúc dạng cây bằng cách dùng một interface cho cả object đơn hoặc object tích hợp.
- Có một interface chung, nếu muốn làm việc với nào thì nó mới duyệt qua và xử lí (Không cần quan tâm đến cấu trúc của những object và composite cấu thành tree → Giúp dễ dàng mở rộng mà không ảnh hưởng đến hệ thống).

4. Decorator pattern:
- Decorator được sử dụng khi chúng ta muốn thêm một hành vi hoặc trạng thái nào đó cho một object trong runtime (bọc các chức năng mới cho một object khi người dùng thêm vào).
- Nếu sử dụng inheritance thông thường, nếu muốn tạo ra một object mới mà thoả những gì chúng ta mong muốn thì chúng ta phải tạo ra một class mà tương ứng với object đó. Còn nếu sử dụng DECORATOR PATTERN thì chỉ cần tạo ra một object gốc và nếu muốn thêm gì cho nó thì chỉ cần bọc cái đó vào là xong.
- Và nếu không có decorator mà muốn thay đôỉ một object thì phải đi qua từng lớp để sửa đổi. Còn nếu có decorator thì chỉ cần sửa đổi một class(class cần sửa đổi) là xong. ==> Dễ maintain hơn.
5. Facade pattern:
- Facade dùng để gói tất cả feature của class con vào một hàm và bỏ nó vào một class, khi sử dụng chỉ cần khởi tạo một class và gọi (sẽ tối ưu hơn nếu để nhiều class ở ngoài và muốn sử dụng thì phải khởi tạo class cho từng cái).
6. Flyweight pattern:
- Flyweight pattern giúp chia sẻ các object giống nhau thay vì tạo mới (giảm sức chứa cho bộ nhớ). 
7. Proxy pattern: dùng để kiểm xoát quyền truy cập của client.
PROXY: Ví dụ có nhiều ứng dụng mà chỉ có một server, khi sử dụng proxy thì những ứng dụng đó nó sẽ connect tới proxy thay vì connect tới server. Điều này làm cho server không biết ứng dụng nào đang được gọi mà chỉ có proxy mới biết và server chỉ biết được địa chỉ ip của proxy chứ không thể nào biết được địa chỉ ip của client (giấu đi thông tin client).
CATCHING: Tường lửa giúp chặn đi những cái độc hại . Ban đầu proxy nhận request để nó kiểm tra nếu mà nó không an toàn thì nó sẽ chặn luôn. (Ví dụ lúc muốn lấy 3 loại dữ liệu khác nhau trên server, nếu không có proxy thì client bắt buộc phải gọi 3 lần, còn nếu có proxy thì lúc mà gửi dữ liệu lên server thì proxy nó sẽ catch lại và lần sau client cần dùng thì nó chỉ cần lấy xuống và trả về ---> giảm thời gian thực thi và chi phí) - BẢO VỀ CLIENT. 
REVERSE PROXY: Thay vì chặn giữa client request ra bên ngoài như catching, thì bây giờ client bên ngoài sẽ gửi request đến server và chặn ở đó và check thông tin, sau đó trả về đúng cho các container (nơi chứa dữ liệu mà client cần tìm).
	- Điều hướng proxy và filter bớt đi.
	- Đóng vai trò như load balancer (cân bằng tải)
	==> BẢO VỆ SERVER.
REMOTE PROXY: Ví dụ có máy đang chạy rất nhiều docker container ví dụ muốn access đến các port đó, nhưng mà ko bao giờ tất cả các port được export ra hết. Thì proxy chỉ mở port cần thiết, sau đó proxy nhận các request đó và điều hướng cho đúng (remote proxy).
PROTECTION PROXY: Ví dụ có một resource cần được bảo vệ và cần authentication để sử dụng --> proxy sẽ check nếu đúng thì cho sử dụng không thì trả về (protection proxy).
VIRTUAL PROXY: Ví dụ có một resource rất lớn và khi create thì rất lâu để có thể create object trong chính resource đó, thì proxy để chuẩn hoá  --- virtual proxy.
SMART PROXY: Thực hiện hành vi bổ sung
	- Thêm chứng năng mà không cần mở rộng.
	- Làm middleware thông minh.
	- Tăng tính mở rộng. 


- Proxy design pattern (những cái trên là nhánh của proxy design pattern trong từng trường hợp cụ thể sẽ có những cách sử dụng khác nhau.
