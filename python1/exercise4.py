a = 21
b = 21
if b > a:
    print("b, a'dan buyuktur")
elif b == a:
    print("b, a'ya esittir")
else: 
    print("b, a'dan kucuktur")

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


def not_getir(score):
    if score >= 90:
        return 'PEKIYI'
    elif score >= 80:
        return 'IYI'
    elif score >= 70:
        return 'ORTA'
    elif score >= 60:
        return 'GECER'
    else: 
        return 'KALDI'

ogrenci_not = int(input('Notunuzu giriniz: '))
ogrenci_notu = not_getir(ogrenci_not)
print(f"Ogrencinin notu: {ogrenci_notu}")

        