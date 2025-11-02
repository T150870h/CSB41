'''
    - Binary search: Tìm kiếm nhị phân
    - Ưu điểm: Một thuật toán nhanh hơn
    - Nhược điểm: yêu cầu danh sách phải được sắp sếp trước
    - Nếu giá trị không tồn tại thì kết quả trả về là -1
Cách hoạt động 
Đặt 2 chỉ số: left (nửa đầu mảng ) và right (nửa cuối mảng)
Tính chỉ số giữa (mid) theo công thức:  mid = (left + right) // 2
'''
my_arr = [1, 2, 3, 4, 5, 6]
key = 5
def Binary_search(arr, key):
    left, right = 0, len(arr) -1 
    while left <= right: 
        mid = (left + right) // 2
        if arr[mid] == key:
            return mid # Trả về vị trị đã tìm thấy 
        elif arr[mid] < key:
            left = mid + 1 # Tìm vế nửa phải
        else:
            right = mid -1 # Tìm nửa bên trái 
    return -1 # Không tìm thấy

result = Binary_search(my_arr , key)
if result != -1:
    print(f"Phần tử {key} đã được tìm thấy tại vị trí {result}")
else:
    print(f"Phần tử {key} không tồn tại trong danh sách")

'''
Nhập danh sách đã sắp xếp và một giá trị x.
Dùng Binary Search để:
In “Có tồn tại” nếu tìm thấy
Ngược lại in “Không tồn tại”.
'''