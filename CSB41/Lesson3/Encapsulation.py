# Encapsulation (Tính đóng gói)
'''
    Tính đóng gói giúp giấu thông tin trong class, chỉ cho phép tương tác qua các 
phương thức. Tăng tính bảo mật và kiểm soát cách dữ liệu thay đổi
'''
class BankAccount():
    def __init__(self, owner, balance):
        self.owner = owner # Tài khoản công khai
        self.__balance = balance # Tài khoản bảo mật

    def get_balance(self):
        return self.__balance

#Tạo 1 đối tượng
account = BankAccount("Hưng", 1000)
# TRuy cập hợp lệ qua phương thức get_balance
print(f"Số dư (Qua phương thức): {account.get_balance()}")

# Thử truy cập trực tiếp 
try:
    print(account.__balance)
except AttributeError as e:
    print("Lỗi", e)


'''
Đề bài:
Tạo lớp BankAccount có:
Thuộc tính số dư (balance) là riêng tư (private).
Các phương thức:
deposit(amount) để nạp tiền.
withdraw(amount) để rút tiền (không cho phép rút quá số dư).
get_balance() để xem số dư.

👉 Viết chương trình thử tạo tài khoản, nạp tiền, rút tiền và in ra số dư cuối cùng.
'''
class BankAccount:
    def __init__(self, balance):
        # Thuộc tính private (Kh truy cập trực tiếp từ bên ngoài)
        self.__balance = balance

    def Deposit(self, amount):
        # Nạp vào tài khoản
        if amount > 0:
            self.__balance += amount
            print(f"Nạp {amount} thành công")
        else: 
            print("Số tiền phải lớn hơn không")

    def Withdraw(self, amount):
        # Rút tiền
        if 0 < amount < self.__balance:
            self.__balance -= amount
            print(f"Rút {amount} thành công")
        else:
            print("Số dư không đủ")

    def get_balance(self):
        # Xem số dư
        return self.__balance

deposit = int(input("Nhập số tiền muốn nạp: "))
withdraw = int(input("Nhập số tiền muốn rút: "))

account = BankAccount(1000) # Số dư ban đầu
account.Deposit(deposit) # Nạp thêm
account.Withdraw(withdraw) # Rút ra
print(f"Số dư cuối cùng: {account.get_balance()}")
