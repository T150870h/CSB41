'''
    OOP (Object oriented programming) là một mô hình dựa trên khái niệm đối tượng
'''
class Nhan_vien():
    def __init__(self, name, age, address):
        # Thuộc tính (acttribute)
        self.name = name
        self.age = age
        self.address = address

    # Phương thức (Method)
    def show_nv(self):
        print(f"Họ và tên: {self.name}, Tuổi: {self.age}, Địa chỉ: {self.address}")

# Truyền dữ liệu 
NvA = Nhan_vien("Hưng", "10", "Hà Nội")
NvB = Nhan_vien("Khánh", "11", "Phú Thọ")

# Gọi ra
NvA.show_nv()

'''
    1. Tên class: Đặt tên cho đối tượng, để có thể gọi ra sử dụng VD: Nhan_vien()
    2. __init__: Phương thức đặc biệt dùng để khởi tạo các thuộc tính, tự động được gọi ra
    3. self: Tham số tham chiếu 
    4. Acttribute - Thuộc tính: Sử dụng để lưu trữ giá trị và có thể thay đổi được
    5. Method - Phương thức: Là hành động thay đổi thuộc tính, hoặc tính năng
'''