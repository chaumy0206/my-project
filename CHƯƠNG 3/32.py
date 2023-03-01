M1=float(input('M1='))
M2=float(input('M2='))
M3=float(input('M3='))
S=int(input('S='))
if S<0:
    print('Vui long nhap lai!!!')
elif S<100:
    print('Phai tra=',S*M1)
elif 101<=S<=150:
    print('Phai tra=',(100*M1)+((S-100)*M2))
elif S>=151:
    print('Phai tra=',round((100*M1)+(50*M2)+((S-150)*M3)))