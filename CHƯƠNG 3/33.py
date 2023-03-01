x=float(input('x='))
y=float(input('y='))
ch=str(input('phep toan:'))
if ch=='+':
    print(x,ch,y,"=",x+y)
elif ch=='-':
    print(x,ch,y,"=",x-y)
elif ch=='*':
    print(x,ch,y,"=",x*y)
elif ch=='/' and y!=0:
    print(x,ch,y,"=",x/y)
else:
    print('Khong hop le')