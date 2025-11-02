'''
    4 loại toán tử
    1. Toán tử số học (+, -, *, /)
        // : Chia lấy phần nguyên
        % : Chia lấy phần dư
        **: Lũy thừa
    2. Toán tử gán 
    = : Gán
    +=: Cộng và gán
    -=: Trừ và gán
    /=: Chia và gán
    *=: Nhân và gán
    %=: Chia lấy dư và gán 
    //=: chia lấy phần nguyên và gán 
    3. Toán tử tử so sánh 
    >, <, >=, <=, != (Khác)
    4. Toán tử Logic
    and: Và logic - Tất cả điều kiện đều phải thỏa mãn
    or: Hoặc logic - Chỉ cần 1 điều kiện thỏa mãn
    not: Phủ định điều kiện
'''
a = 10
b = 3
a //= b # a = a // b => a = 10 // 3 => a = 3
print(a)
print(a//b)
print(a % b)

c = 100
d = 1000
if c == d or c < d and c > d:
    print(True)
else:
    print(False)