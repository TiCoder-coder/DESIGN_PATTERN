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
- Thay đổi object dễ dàng mà không cần sửa code
3. Builder pattern:
- Giúp chia nhỏ các constructer và có thể khởi tạo một object theo nhiều hướng khác nhau.
-Tách logic xây dựng product thành nhiều bước nhỏ.

4.Prototype pattern: Dùng để giải quyết ván đề tạo object mới nhưng chỉ khác object cũ chỉ vài thuộc tính, lúc đó ta dùng prototype pattern code sẽ đẹp và ngọn nhẹ hơn.

5.Singleton: 
- Đảm bảo rằng 1 class chỉ tạo ra duy nhất một instance cho toàn bộ chương trình và đồng thời cung cấp một điểm truy cập toàn cục đến instance đó.
- Dùng khi Logger, kết nối database,...