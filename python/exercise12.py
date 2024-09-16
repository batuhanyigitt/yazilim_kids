from datetime import datetime, timedelta

now = datetime.now()
current_year = now.year
current_month = now.month
current_day = now.day

byear = int(input("Dogum yilinizi giriniz: "))
bmonth = int(input("Dogum ayinizi giriniz: "))
bday = int(input("Dogum gununuzu giriniz: "))
bname = str(input("Adinizi giriniz: "))

if byear < current_year:

    age_years = current_year - byear
    
    if bmonth > current_month or (bmonth == current_month and bday > current_day):
        age_years -= 1
    
    if bmonth > current_month or (bmonth == current_month and bday > current_day):
        age_months = (12 - bmonth) + current_month - 1
    else:
        age_months = current_month - bmonth
    

    if bday > current_day:
        previous_month_last_day = (now.replace(day=1) - timedelta(days=1)).day
        age_days = previous_month_last_day - bday + current_day
    else:
        age_days = current_day - bday

    print(f"İsmin {bname}, yaşın {age_years}, aylık {age_months}, ve günlük {age_days}.")
else:
    print("Yanlış bilgi girdiniz.")







from datetime import datetime
now = datetime.now()
current_year = int(now.strftime("%Y"))
current_month = int(now.strftime("%m"))
current_day = int(now.strftime("%d"))

byear = int(input("Dogum yilinizi yaziniz: "))
bmonth = int(input("Dogum ayinizi yaziniz: "))
bday = int(input("Dogum gununuzu yaziniz: "))
bname = str(input("Adinizi yaziniz: "))
birth_date = datetime(byear, bmonth, bday)
current_date = datetime(current_year, current_month, current_day)

age_years = current_date.year - birth_date.year
age_months = current_date.month - birth_date.month
age_days = current_date.day - birth_date.day
if age_days < 0:
    age_months -= 1
    age_days += (birth_date.replace(month=birth_date.month + 1) - birth_date).days

if age_months < 0:
    age_years -= 1
    age_months += 12
total_days = (current_date - birth_date).days
if age_years > 100:
    print("Kimse bu kadar uzun yaşayamaz!")
else:
    print(f"Ismin {bname}, yasin {age_years} yil, {age_months} ay, {age_days} gun")
    print(f"Toplam {total_days} gunluksun")



from datetime import datetime
def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Lütfen geçerli bir sayı girin.")
def main():
    now = datetime.now()
    current_year = now.year
    current_month = now.month
    current_day = now.day
    byear = get_int_input("Doğum yılınızı giriniz: ")
    bmonth = get_int_input("Doğum ayınızı giriniz: ")
    bday = get_int_input("Doğum gününüzü giriniz: ")
    bname = input("Adınızı giriniz: ")

    if not (1 <= bmonth <= 12):
        print("Yanlış ay girdiniz. Ay 1 ile 12 arasında olmalıdır.")
        return
    if not (1 <= bday <= 31):  
        print("Yanlış gün girdiniz. Gün 1 ile 31 arasında olmalıdır.")
        return
    age_years = current_year - byear
    age_months = current_month - bmonth
    age_days = current_day - bday

    if age_days < 0:
        age_months -= 1
        age_days += 30  

    if age_months < 0:
        age_years -= 1
        age_months += 12
    print(f"İsminiz {bname} ve yaşınız {age_years} yıl {age_months} ay {age_days} gün.")
if __name__ == "__main__":
    main()









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
    
    

