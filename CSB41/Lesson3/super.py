# Tạo 1 lớp Person
# class Person():
#     def __init__(self, name, age, address):
#         # Thuộc tính Person
#         self.name = name
#         self.age = age
#         self.address = address 

#     def introduce(self):
#         print(f"Tên tôi là: {self.name} và tôi {self.age} tuổi")
# newPeson = Person("Hưng", "10", "Hà Nội")
# newPeson.introduce()

# # Lớp Student kế thừa các thuộc tính của Person
# class Student(Person): 
#     def __init__(self, name, age, address, Student_id):
#         # Sử dụng hàm super để kế thừa và phần biệt thuộc tính của cha (Person)
#         super().__init__(name, age, address) # Gọi hàm khởi tạo của Person
#         self.Student_id = Student_id

#     # Phương thức sử dụng thuộc tính cha (Person)
#     def show_student(self):
#         print(f"Tên học sinh là: {self.name}, tuổi: {self.age}, địa chỉ: {self.address}, ID: {self.Student_id}")

# # Tạo đối tượng 
# newStudent = Student("Ngân", "12", "Hưng Yên", "1")
# newStudent.show_student()


'''
Đề bài:
Tạo lớp Person có thuộc tính name và phương thức introduce() in ra "Tôi là <tên>".
Tạo lớp Student kế thừa Person, thêm phương thức study() in ra "<tên> đang học bài".
👉 Viết chương trình tạo đối tượng Student, gọi cả introduce() và study().
'''
class Person():
    def __init__(self, name):
        self.name = name 
    def introduce(self):
        print(f"Tôi tên là: {self.name}")

class Student(Person):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def study(self):
        print(f"{self.name} đang học có độ tuổi là {self.age}")

name = input("Họ và tên là: ")
age = input("Tuổi của tôi là: ")

Student1 = Student(name, age)
Student1.study()
