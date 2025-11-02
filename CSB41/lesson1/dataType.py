'''
    1. Các kiểu dữ liệu nguyên thủy
        - Kiểu chuỗi (string - str): Lưu trữ các chuỗi ký tự
        - float (Số thực - float): Lưu trữ các số thực
        - integer (Số nguyên - int): Lưu trữ các số nguyên 
        - boolean (Kiểu logic): True / False

    2. Kiểu dữ liệu tham chiếu 
        - List (Danh sách)
        - Dictionary (Từ điểm)
    3. Kiểm tra kiểu dữ liệu sử dụng: type()
'''
name = "Hưng Đẹp trai"
num = 3.14
num_int = 10
isStudent = True
print("Tên tôi là: ", name)
print("Kiểu số thực: ", num)
print("Kiểu số nguyên: ", num_int)
print("Kiểu Logic: ", isStudent)

# Ví dụ về kiểu dữ liệu tham chiếu 
# List: Có thể lưu trữ các các kiểu dữ liệu nguyên thủy cũng như tham chiếu
my_list = [1, 2, 3, 4, 5, 6, 7, "Hưng", True, [3, 56, 7]]
# Item (Giá trị - Phần tử): ký hiệu ()   
# index (vị trí - thứ tự): Bắt đầu từ 0
print("Danh sách: ", my_list)
print("Giá trị được truy xuất ở ví trí 7: ",my_list[7])

#  Dictionary (Từ điểm)
myDictionary = {
    "key": "Value",
    "name": "Thành Hưng",
    "age": 10,
}
print("Từ điển: ", myDictionary)