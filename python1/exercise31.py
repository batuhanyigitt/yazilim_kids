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

