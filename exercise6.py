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