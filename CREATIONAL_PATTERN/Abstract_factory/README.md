Mô phỏng quy trình chạy:
- Ban đầu sẽ có 2 abstract factory là Enclosure_factory và Animal_factory đùng dể  khởi tạo ban đầu.
- Sau đó Factory_Create sẽ tạo ra các animal và enclisure từ Enclosure_factory và Animal_factory.
- Và từ đó nó sẽ tạo ra các enclosure (Enlosure_Big_Size, Enlosure_Big_Size) và animal(FourLegsAnimal, TwoLegsAnimal) momg muốn --> tạo ra zoo(create_Zoo_Animal_Have_2_Legs, create_Zoo_Animal_Have_4_Legs) momg muốn.