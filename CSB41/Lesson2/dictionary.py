'''
    1. Khai báo từ điển 
    2. Truy cập phần tử
    3. Thêm hoặc sửa phần tử 
    4. Xóa phần tử
    5. Duyệt qua từ điển 
'''
#  Dictionary (Từ điểm)
myDictionary = {
    "key": "Value",
    "name": "Thành Hưng",
    "age": 10,
    "new": {
        "age": 20,
    }
}
print("Từ điển: ", myDictionary)

# Truy cập phần tử
print(myDictionary["name"])
print(myDictionary["age"])
print(myDictionary["new"]["age"])

# Thêm và sửa phần tử 
myDictionary["name"] = "Thành Hưng ĐZ"
myDictionary["age"] = 30
print(myDictionary)

# Xóa phần tử del, pop()

# Duyệt qua Từ điển
'''
Dùng for để duyệt và in ra tên + điểm của học sinh có điểm 
cao nhất trong scores.
'''
# Nhập số lượng học sinh 
n = int(input("Nhập số lượng học sinh: "))
# Khởi tạo danh sách rỗng 
scores = {}

# Nhập dữ liệu từ bàn phím 
for index in range(n):
    name = input(f"Nhập tên học sinh thứ {i+1}: ")
    score = input(f"Nhập nhập điểm của học sinh {name}: ")
    # Thêm vào từ điển
    scores[name] = score

# Tìm học sinh có số điểm cao nhất
max_name = None
max_score = -1

for name, score in scores.item():
    if score > max_score:
        max_score = score
        max_name = name

print(f"Học sinh có điểm cao nhất là {max_name} với {max_score} điểm")

