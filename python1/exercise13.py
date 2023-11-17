'''
from datetime import datetime
now = datetime.now()
year = now.strftime("%Y")
month = now.strftime("%m")

byear = int(input("Dogum yilinizi giriniz:"))
bmonth = int(input("dogum ayinizi giriniz: "))
bname = str(input("Adinizi giriniz:"))
year = int(year)
month = int(month)

if(byear < year):
    if(bmonth < month):
        x = year - byear
        y = month - bmonth 
        z = bname 
        print(f"ismin {z} ve yasin {x} ve ayliksin {y}")
    else: 
        x = (year - byear) - 1 
        y = (12 - bmonth) + month
        z = bname 
        print(f"ismin {z} ve yasin {x} ve de ayliksin {y}")
else:
    print("yanlis bilgi girdiniz")


num = int(input("Enter a number: "))
mod = num % 2
if mod > 0:
    print("This is an odd number.")
else: 
    print("This is an even number.")
'''



