Toan=int(input())
Ly=int(input())
Hoa=int(input())
ĐTB=((Toan*2)+(Ly*3)+Hoa)/6
if ĐTB<3:
    print("Kém")
elif 3<=ĐTB<5:
    print("Yếu")
elif 5<=ĐTB<6:
    print("Trung bình")
elif 6<=ĐTB<7:
    print("Trung bình Khá")
elif 7<=ĐTB<8:
    print("Khá")
elif 8<=ĐTB<9:
    print("Giỏi")
elif 9<=ĐTB<=10:
    print('Xuất sắc')
    