class Car:
    def __init__(self, marka, model):
        self.marka = marka 
        self.model = model 
        
    def move(self):
        print("Araba hareket ediyor. ")
        

class Atarabasi:
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model 
    
    def move(self):
        print("Sergen kos yaris basladi")
        

class Plane: 
    def __init__(self, marka, model):
        self.marka = marka 
        self.model = model 
        
    def move(self):
        print("ucak ucuyor")
        

car1 = Car("Tofask", "sahin")
Atarabasi1 = Atarabasi("Ingiliz", "tay")
plane1 = Plane("Boeing", "747")

