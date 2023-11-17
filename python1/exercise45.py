import random

class TuranOyunu:
    def __init__(self):
        self.altin = 100
        self.ordu = 10
        self.toprak = 100

    def savas(self):
        dusman_ordu = random.randint(1, 20)
        print(f"Düşman ordusu sayısı: {dusman_ordu}")

        if self.ordu > dusman_ordu:
            print("Savaşı kazandınız! Zafer kazandınız ve düşman ordusunu geri püskürttünüz.")
            self.altin += 50
        else:
            print("Savaşı kaybettiniz. Düşman ordusu Turan İmparatorluğu'nu istila etti.")
            self.altin -= 20

    def maden_islet(self):
        toplam_maden = random.randint(5, 15)
        print(f"Toplamda {toplam_maden} ton maden bulundu.")

        self.altin += toplam_maden * 2
        self.toprak -= toplam_maden

    def durum_goster(self):
        print(f"Altın miktarı: {self.altin} birim")
        print(f"Ordu sayısı: {self.ordu} asker")
        print(f"Toprak miktarı: {self.toprak} birim")

    def oyunu_oyna(self):
        while self.altin > 0 and self.ordu > 0 and self.toprak > 0:
            print("\nTuran İmparatorluğu'na hoş geldiniz!")
            print("1. Savaş")
            print("2. Maden İşlet")
            print("3. Durumu Göster")
            print("4. Çıkış")

            secim = input("Yapmak istediğiniz eylemi seçin (1-4): ")

            if secim == "1":
                self.savas()
            elif secim == "2":
                self.maden_islet()
            elif secim == "3":
                self.durum_goster()
            elif secim == "4":
                print("Oyunu bitiriyorsunuz. Güle güle!")
                break
            else:
                print("Geçersiz bir seçim yaptınız. Lütfen tekrar deneyin.")

if __name__ == "__main__":
    turan_oyunu = TuranOyunu()
    turan_oyunu.oyunu_oyna()
