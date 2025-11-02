'''
    Danh sách (list)
        1.Cấu tạo của list
        2. TRuy cập phần tử của list
        3. Thêm phần tử vào danh sách
        4. Xóa phần tử ra khỏi danh sách 
        5. Độ dài danh sách
        6. Lặp qua danh sách
'''
# 1. Cấu tạo của list
my_list = [1, 2, 3, "Hưng", True]
# index- kí hiệu: []: Thứ tự và vị trí, bắt đầu từ 0 
# item - kí hiệu: (): Các giá trị được khai báo 
epmty_list = [] 
# 2. TRuy cập phần tử bằng index
num = my_list[3]
print(num)

'''
Nhập từ bàn phím, Tính tổng các phần tử trong list
Viết chương trình nhập một list số nguyên và dùng for để tính
tổng các phần tử.
'''
lst = []
for index in range(1, 6):
    lst.append(index)
print(lst)

# Nhập từ bàn phím
n = int(input("Nhập số phần tử muốn thêm vào list: ")) # 10 
lit = [] # => độ dài của list là 10
for index in range(n): 
    x = int(input(f"Nhập phần tử thứ {index + 1}: "))
    lit.append(x)
print("List sau khi nhập: ", lit)
tong = 0
for num in lit:
    tong += num
print(f"Tổng các phần từ trong list là: {tong}")

# Cách 2
numbers = input("Nhập các số nguyên (cách nhau bởi khoảng trắng): ")
list_num = [int(x) for x in numbers.split()]
tong = 0
for num in lit:
    tong += num
print(f"Tổng các phần từ trong list là: {tong}")

# 3. Thêm phần tử: append(), insert()
print(my_list)
my_list.insert(2, "Hưng Đz") # Thay thế phần tử "Hưng Đz" vào vị trị index[2]
print(my_list)
# 4. Xóa danh sách clear(), remove(), pop(), del
