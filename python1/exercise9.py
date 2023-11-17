class MyEvenNumbers:
    def __init__(self, start=2, end=20):
        self.start = start if start % 2 == 0 else start + 1
        self.end = end if end % 2 == 0 else end - 1
        self.current = self.start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.end:
            x = self.current
            self.current += 2
            return x
        else:
            raise StopIteration

myclass = MyEvenNumbers(start=4, end=20)

for x in myclass:
    print(x)





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
            
           
        
       