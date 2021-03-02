traxanhc2=9000
sting=11000
pepsi=10000
warrior=13000
ncsuoi=5000
charge=0
list=["traxanhc2","sting","pepsi","warrior","ncsuoi"]
tienvao=int(input("nhap so tien vao: "))
print(list)
nuocdcchon=int(input("nhap so nuoc ban muon mua: "))
s1=list.index("traxanhc2")
s2=list.index("sting")
s3=list.index("pepsi")
s4=list.index("warrior")
s5=list.index("ncsuoi")
if nuocdcchon == s1:
    charge=tienvao-traxanhc2
elif nuocdcchon == s2:
    charge=tienvao-sting
elif nuocdcchon == s3:
    charge=tienvao-pepsi
elif nuocdcchon == s4:
    charge=tienvao-warrior
elif nuocdcchon == s5:
    charge=tienvao-ncsuoi
else:
    print("xin hay thoat ra va nhap lai")
while nuocdcchon >= 0 and nuocdcchon <= 4:
    if charge >= 0:
        print("Mua hang thanh cong. So tien con lai ban co la", charge)
    else: print("Ban khong du tien de mua thuc uong nay")
    break