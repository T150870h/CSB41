# Abstraction: Tính trừu tượng 
'''
    Trừu tượng giúp ẩn đi các chi tiết phức tạp, Chỉ cung
cấp những gì cần thiết. thường được thực hiện thông qua
các lớp TRừu tượng hoặc giao diện
'''
from abc import ABC, abstractmethod
 # Tạo lớp trừu tượng (Lớp cha)
class Vehicel(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

# Lớp con: Ô tô
class Car(Vehicel):
    def start(self):
        print("Ô tô khởi động bằng chìa")
    def stop(self):
        print("Ô tô dừng lại bằng phanh")

# Lớp con: xe đạp 
class Bike(Vehicel):
    def start(self):
        print("Xe đạp đặp băng chân")
    def stop(self):
        print("Xe đạp bó phanh để dừng lại")

# Đặt biến lưu class
car = Car()
bike = Bike()
# Gọi 
car.start()
car.stop()
bike.start()
bike.stop()