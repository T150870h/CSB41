# Polymorphism: Tính da hình
'''
Đa hình cho phép sử dụng một phương thức theo nhiều cách khác nhau.
'''
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "go go"
class Cat(Animal):
    def speak(self):
        return "Meo meo"
class Pig(Animal):
    def speak(self):
        return "Ụi ịt"

# Hàm đa hình
def animal_sound(animal):
    print(animal.speak())

# Tạo biến lưu lớp 
dog = Dog()
cat = Cat()
pig = Pig()
# Gọi hàm animal_sound() với các đối tượng khác nhau
animal_sound(dog)
animal_sound(cat)
animal_sound(pig)