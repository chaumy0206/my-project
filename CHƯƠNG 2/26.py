tên=input("Họ ten:")
SốNgàyCông=int(input("So ngay cong:"))
ĐơnGiáNgàyCông=int(input("Don gia ngay cong:"))
HệSốPhụCấp=float(input("He so phu cap:"))
TạmỨng=int(input("Tam ung:"))
Lương=ĐơnGiáNgàyCông*SốNgàyCông*HệSốPhụCấp
print("Nhan vien",tên,end=",")
print("Co tien Luong=",Lương,end=",")
print("Tam ung=",TạmỨng,end=",")
print("va Thuc linh=", Lương-TạmỨng)