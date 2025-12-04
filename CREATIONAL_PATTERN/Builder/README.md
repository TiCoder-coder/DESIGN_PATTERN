Mô phỏng quá trình thực thi:
- Ban đầu sẽ có một class Builder_factory sé định nghĩa các phương thức cần thiết để xây dựng.
- Sau đó class Builder sẽ định nghĩa các phương thức abstract để xây dựng một căn nhà (mỗi thuộc tính sẽ có một hàm build riêng).
- Và class House_builder sẽ overwirte lại các phương thức ở trong class Builder để xây dựng một căn nhà.
- Và file Implement.py sẽ gọi lại tất cả các phương thức và thực thi