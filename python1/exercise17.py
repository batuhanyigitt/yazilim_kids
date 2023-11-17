'''
basamak = 10
bosluk = basamak - 1 
i = 1

while i <= basamak:
    print(" "* bosluk + "*"*(2*i-1))
    bosluk -= 1
    i += 1 



fil = 5
i = 1

while i <= fil:
    if i == 1 or i == fil:
        print("*"*fil)
    else:
        print("*"+ " " * (fil -2) + "*")
    i += 1

def selam():
    print("Merhaba")

selam()
'''





def toplama(a, b):
    sonuc = a + b
    return sonuc 

toplam_sonuc = toplama(3, 5)
print("Toplam sonuc: ", toplam_sonuc)
