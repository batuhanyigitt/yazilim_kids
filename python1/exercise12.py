def ucgen_tanimlama(kenar1, kenar2, kenar3):
    if kenar1 == kenar2 == kenar3:
        return "Eskenar Ucgen"
    elif kenar1 == kenar2 or kenar1 == kenar3 or kenar2 == kenar3:
        return "Ikizkenar Ucgen"
    else: 
        return "Cesitkenar Ucgen"

kenar1 = float(input("1. Kenar: "))
kenar2 = float(input("2. Kenar: "))
kenar3 = float(input("3. Kenar: "))

ucgen_yazdirma = ucgen_tanimlama(kenar1, kenar2, kenar3)
print(f"Ucgenin cesidi: {ucgen_yazdirma}")


from datetime import datetime 
now = datetime.now()
year = now.strftime("%Y")
month = now.strftime("%m")

byear = int(input("Dogum yilinizi giriniz: "))
bmonth = int(input("Dogum ayinizi giriniz: "))
bname = str(input("Adinizi giriniz: "))
year = int(year)
month = int(month)

if (byear < year):
    if(bmonth < month):
        x = year - byear
        y = month - bmonth 
        z = bname
        print(f"ismin {z} ve yasin {x} ve ayliksin {y}")
    else:
        x = (year - byear) - 1
        y = (12 - bmonth) + month
        z = bname
        print(f"ismin {z} ve yasin {x} ve ayliksin {y}")
else: 
    print("yanlis bilgi girdiniz")
    
    
    
    from datetime import datetime
now = datetime.now()
year = now.strftime("%Y")
month = now.strftime("%m")

byear = int(input("Dogum yilini giriniz: "))
bmonth = int(input("Dogum ayini giriniz: "))
bname = str(input("Adinizi giriniz: "))
year = int(year)
month = int(month)

if (byear < year):
    x = year - byear
    y = month - bmonth
    z = bname 
    print(f"ismin {z} ve yasin {x} ve ayliksin {y}")
    

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
    
    

num = int(input("sayi giriniz:"))
if num%2 == 0:
    if num%3 == 0:
        print("sayi 2'ye ve 3'e tam bolunur")
    else:
        print("sayi 2'ye tam bolunur, fakat 3'e bolunmez")
else:
    if num%3 == 0:
        print("sayi 3'e tam bolunur, fakat 2'ye bolunmez")
    else: 
        print("hicbirine tam bolunmez")
        
        