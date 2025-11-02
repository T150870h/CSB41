'''
    Tìm kiếm tuần tự (Linear Search) - Tìm kiếm tuyến tính
Mô tả:
- Là phương pháp đơn giản nhất: Kiểm tra từ phần tử trong mảng từ đầu cho đến 
cuối cho đến khi tìm thấy phần tử cần tìm 
- Ưu điểm: Không cần sắp xếp trước, Áp dụng được cho mọi loại mảng
- Nhược điểm: Chạy lâu khi gặp mảng danh sách lớn
- Khi không tìm thấy giá trị cho kết quả là -1
'''
arr = [76, 1, 24, 78, 2, 10, 100, 27]
key = 2
def Linear_search(arr, key): 
    for index in range(len(arr)):
        if arr[index] == key:
            return index # Trả về vị trí tìm thấy
    return -1 # Nếu không tìm thấy

result = Linear_search(arr, key)
if result != -1:
    print(f"Phần tử {key} được tìm thấy tại vị trí {result}")
else:
    print(f"Giá trị {key} không tồn tại trong mảng")


'''
Đề bài:
Nhập vào một danh sách số và một giá trị cần tìm.
Dùng Linear Search để in ra:
Vị trí đầu tiên tìm thấy giá trị đó.
Hoặc thông báo nếu không tìm thấy.
'''
numbers = [5, 8, 10, 5, 9 , 2]
key = int(input("Nhập số cần tìm: "))
def search_number(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

index_number = search_number(numbers, key)
if index != -1:
     print(f"Phần tử {key} được tìm thấy tại vị trí {index_number}")
else:
    print(f"Giá trị {key} không tồn tại trong mảng")