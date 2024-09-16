def bolunebilirlik_kontrolu(sayi):
    if sayi % 2 == 0 and sayi % 3 == 0 and sayi % 4 == 0:
        return "2, 3 ve 4'e tam bölünebiliyor"
    elif sayi % 2 == 0:
        return "Sadece 2'ye tam bölünebiliyor"
    elif sayi % 3 == 0:
        return "Sadece 3'e tam bölünebiliyor"
    elif sayi % 4 == 0:
        return "Sadece 4'e tam bölünebiliyor"
    else:
        return "Hiçbirine tam bölünemiyor"


sayi = int(input("bir sayi yaziniz"))
sonuc = bolunebilirlik_kontrolu(sayi)
print(sonuc)
