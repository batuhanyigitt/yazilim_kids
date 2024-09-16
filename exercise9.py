class AsalSayilar:
    def __init__(self, limit):
        self.limit = limit 
        self.tanimla = [True] * (limit + 1)
        self.tanimla[0] = self.tanimla[1] = False
        self.current = 2 
        
    def asal_uret(self):
        for start in range(2, int(self.limit**0.5) + 1):
            if self.tanimla[start]:
                for multiple in range(start*start, self.limit+1, start):
                    self.tanimla[multiple] = False
                    
    def __iter__(self):
        self.asal_uret()
        return self
    
    def __next__(self):
        while self.current <= self.limit:
            if self.tanimla[self.current]:
                asal = self.current
                self.current += 1 
                return asal
            self.current += 1 
        raise StopIteration
    
    
asal_uret = AsalSayilar(40)
for asal in asal_uret:
    print(asal)
                
    
    
    
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




class PrimeNumberGenerator:
    def __init__(self, limit):
        self.limit = limit
        self.sieve = [True] * (limit + 1)
        self.sieve[0] = self.sieve[1] = False  
        self.current = 2

    def generate_primes(self):
        for start in range(2, int(self.limit**0.5) + 1):
            if self.sieve[start]:
                for multiple in range(start*start, self.limit + 1, start):
                    self.sieve[multiple] = False

    def __iter__(self):
        self.generate_primes()
        return self

    def __next__(self):
        while self.current <= self.limit:
            if self.sieve[self.current]:
                prime = self.current
                self.current += 1
                return prime
            self.current += 1
        raise StopIteration

prime_gen = PrimeNumberGenerator(50)
for prime in prime_gen:
    print(prime)

