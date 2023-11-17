class Engine:
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type

    def start(self):
        print("Engine started.")

    def stop(self):
        print("Engine stopped.")


class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.engine = None

    def move(self):
        print(f"{self.brand} {self.model} is in motion.")

    def set_engine(self, fuel_type):
        self.engine = Engine(fuel_type)


class Car(Vehicle):
    def move(self):
        print(f"{self.brand} {self.model} is driving!")

    def honk(self):
        print("Honk! Honk!")


class Boat(Vehicle):
    def move(self):
        print(f"{self.brand} {self.model} is sailing!")

    def anchor(self):
        print("Anchor dropped.")


class Plane(Vehicle):
    def move(self):
        print(f"{self.brand} {self.model} is flying!")

    def take_off(self):
        print("Taking off.")


# Create instances of each class
car1 = Car("Ford", "Mustang")
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boeing", "747")

# Set engines for vehicles
car1.set_engine("Gasoline")
boat1.set_engine("Diesel")
plane1.set_engine("Jet fuel")

# Perform actions on each vehicle
car1.move()
car1.honk()
car1.engine.start()

boat1.move()
boat1.anchor()
boat1.engine.start()

plane1.move()
plane1.take_off()
plane1.engine.start()






'''
kelime = "kosmak"

for x in kelime:
    print(x)
    
y = "kosmak"
print(len(y))



class Car:
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model
    
    def move(self):
        print("Araba hareket ediyor")
    
class Boat: 
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model
    
    def move(self):
        print("Tekne hareket ediyor")
        
class Plane:
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model
    
    def move(self):
        print("Ucak hareket ediyor")

car1 = Car("BMW", "Mustang")
boat1 = Boat("Yamaha", "Yat")
plane1 = Plane("Boeing", "747")

for x in (car1, boat1, plane1):
    x.move()

    
    
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        pass


class Car(Vehicle):
    def move(self):
        print(f"{self.brand} {self.model} hareket ediyor!")


class Boat(Vehicle):
    def move(self):
        print(f"{self.brand} {self.model} hareket ediyor!")


class Plane(Vehicle):
    def move(self):
        print(f"{self.brand} {self.model} hareket ediyor!")


car1 = Car("Ford", "Mustang")
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boeing", "747")

vehicles = [car1, boat1, plane1]

for vehicle in vehicles:
    vehicle.move()
'''




class Engine:
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type

    def start(self):
        print("Engine started.")

    def stop(self):
        print("Engine stopped.")


class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.engine = None

    def move(self):
        print(f"{self.brand} {self.model} is in motion.")

    def set_engine(self, fuel_type):
        self.engine = Engine(fuel_type)


class Car(Vehicle):
    def move(self):
        print(f"{self.brand} {self.model} is driving!")

    def honk(self):
        print("Honk! Honk!")


class Boat(Vehicle):
    def move(self):
        print(f"{self.brand} {self.model} is sailing!")

    def anchor(self):
        print("Anchor dropped.")


class Plane(Vehicle):
    def move(self):
        print(f"{self.brand} {self.model} is flying!")

    def take_off(self):
        print("Taking off.")


# Create instances of each class
car1 = Car("Ford", "Mustang")
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boeing", "747")

# Set engines for vehicles
car1.set_engine("Gasoline")
boat1.set_engine("Diesel")
plane1.set_engine("Jet fuel")

# Perform actions on each vehicle
car1.move()
car1.honk()
car1.engine.start()

boat1.move()
boat1.anchor()
boat1.engine.start()

plane1.move()
plane1.take_off()
plane1.engine.start()






class Car:
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model
    
    def move(self):
        print("Araba hareket ediyor")
    
class Boat: 
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model
    
    def move(self):
        print("Tekne hareket ediyor")
        
class Plane:
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model
    
    def move(self):
        print("Ucak hareket ediyor")

car1 = Car("BMW", "Mustang")
boat1 = Boat("Yamaha", "Yat")
plane1 = Plane("Boeing", "747")

for x in (car1, boat1, plane1):
    x.move()

    
    
    
    class Car:
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model
    
    def move(self):
        print("Araba hareket ediyor")
    
class Boat: 
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model
    
    def move(self):
        print("Tekne hareket ediyor")
        
class Plane:
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model
    
    def move(self):
        print("Ucak hareket ediyor")

car1 = Car("BMW", "Mustang")
boat1 = Boat("Yamaha", "Yat")
plane1 = Plane("Boeing", "747")

for x in (car1, boat1, plane1):
    x.move()

    
    
    
'''
class MyClass:
    x = 5 
    y = "Batuhan"
p = MyClass()
print(p.y)


class Calisan:
    def __init__(self, isim, soyisim, maas, departman):
        self.isim = isim
        self.soyisim = soyisim
        self.maas = maas
        self.departman = departman 
    def maasiArttir(self, oran):
        self.maas += oran 
        return f"{self.isim}in yeni maasi {self.maas}"

calisan1 = Calisan("Eren", "yilmaz", 1000, "Yazilim")
calisan2 = Calisan("Batuhan", "yigit", 2000, "Yazilim")

print(calisan1.maasiArttir(500))
print(calisan2.maasiArttir(1000))
'''

class Kisi:
    def __init__(self, ad, soyad, sehir, yas, egitim):
        self.ad = ad
        self.soyad = soyad
        self.sehir = sehir
        self.yas = yas 
        self.egitim = egitim

kullanici1 = Kisi("Batuhan", "Yigit", "Poznan", 26, "Yuksek Lisans")


print("Kullanıcı 1:")
print("Ad:", kullanici1.ad)
print("Soyad:", kullanici1.soyad)
print("Sehir:", kullanici1.sehir)
print("Yas:", kullanici1.yas)
print("Egitim:", kullanici1.egitim)
print()


        