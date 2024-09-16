import time

def sayac(baslangic_sayisi, mesaj):
    sayac = baslangic_sayisi
    while sayac > 0: 
        print(sayac)
        sayac -= 1 
        time.sleep(1)
    print(mesaj)
    
baslangic_sayisi = int(input("geri sayim icin sayi giriniz: "))
mesaj = input("mesajinizi giriniz: ")
sayac(baslangic_sayisi, mesaj)