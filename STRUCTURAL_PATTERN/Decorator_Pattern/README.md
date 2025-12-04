Mô phỏng cấu trúc kế thừa:
- Ban đầu sẽ khởi tạo một class IMilkTea
- Và class MilkTea (trà sữa ban đầu lúc chưa có topping) và class MilkTeaDecorator (topping cho trà sữa) 2 class này sẽ kế thừa lại IMilkTea.
- Và các topping sẽ kế thừa lại MilkTeaDecorator (kế thừa chung 1 class -- Điều này là một điểm đặc biệt của decorator design pattern là nó sẽ cho các topping kế thừa chung một class nếu cần sửa đổi chỉ cần sửa đổi một class là xong).
