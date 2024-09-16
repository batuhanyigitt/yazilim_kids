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