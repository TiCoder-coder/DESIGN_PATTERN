Mô phỏng cấu trúc kế thừa:
- Ban đầu sẽ khởi tạo một class IPrototype class này sẽ định nghĩa các abstract method cho protopy và nó sẽ được overwrite lại ở class Prototype.

Mô phỏng quá trình thực thi:
- Client sẽ tạo ra một object đầu tiên, nếu object thứ 2 tạo mà chỉ khác object đầu tiên vài thuộc tính thì nó prototype sẽ tiến hành copy và thay đổi lại các thuộc tính cần thiết. Điều này rất hữu dụng ==> Không cần tạo lại nguyên một object từ đầu ==> Tiết kiệm time và bộ nhớ.