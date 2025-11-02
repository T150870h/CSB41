class Car():
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage
    def show(self):
        print(f"Một chiếc xe {self.color} chạy được {self.mileage} km")
car1 = Car("xanh", 20000)
car2 = Car("đỏ", 30000)
car1.show()
car2.show()