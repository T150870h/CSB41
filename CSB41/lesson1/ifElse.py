'''
    Câu lệnh điều kiện rẽ nhánh
        - TH1: 1 điều kiện 
        - TH2: 1 điều kiện và phần còn lại 
        - TH3: Nhiều điều kiện khác nhau và phần còn lại
'''
# TH1
a = 10 
b = 20 
if a < b:
    print(True)

# TH2
if a == b:
    print(False)
else:
    print(True)

#TH3
if a > b:
    print("A lớn hơn b")
elif a == b:
    print("A bằng b")
elif a >= b:
    print("A lớn hơn hoặc bằng b")
else:
    print("Các trường hợp còn lại")