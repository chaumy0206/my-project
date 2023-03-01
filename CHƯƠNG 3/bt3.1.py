a = float(input("nhập số a :"))
b = float(input("nhập số b :"))
c = float(input("nhập số c :"))
max = a
if b > max : 
    max = b
if c > max :
    max = c
min = a
if b < min : 
    min = b
if c < min :
    min = c
print("giá trị lớn nhất là :", max,)
print("giá trị nhỏ nhất là :", min,)