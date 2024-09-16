from translate import Translator

def get_translation(input_text, source_lang, target_lang):
    translator = Translator(from_lang=source_lang, to_lang=target_lang)
    translation = translator.translate(input_text)
    return translation
print("Hello")
print("naber")


import turtle

import colorsys

t = turtle.Turtle()

s = turtle.Screen().bgcolor('black')

t.speed(0)

n = 70

h = 0

for i in range(360):

    c = colorsys.hsv_to_rgb(h, 1, 0.8)

    h+= 1/n

    t.color(c)

    t.left(1)

    t.fd(1)

    for j in range(2):

        t.left(2)

        t.circle(100)
        
        
        
print("Hello")
print("Selam nasilsin nasil gidiyor")


kisi = {"isim": "batuhan", "soyisim": "yigit", "yas": 27, "sehir": "Adana"}



''''
ilkliste = ["elma", "armut", "muz", "karpuz", "kavun"]
print(ilkliste)
print(ilkliste[:2])
print(ilkliste[1])
print(ilkliste[0])


yeniliste = ["CS", "101", "Lol", "Valorant", "fifa"]
if "CS" in yeniliste:
    print("CS var")

'''


firstdict = {
    "marka" : "Ford",
    "model" : "Mustang",
    "year": 1964
}

print(firstdict)


cars = {
    "araba1" : {
        "marka" : "toyota",
        "year" : 2000
    },
    "araba2" : {
        "marka" : "ford", 
        "year" : 2002
    },
    "araba3" : {
        "marka" : "bmw",
        "year" : 2002
    },
}
print(cars)



yeniliste = ["CS", "101", "batak", "LoL", "Valorant", "Rust"]
if "batak" in yeniliste:
    print("evet, bu listede")



sehir = ["Istanbul", "Ankara", "Izmir", "Bursa", "Adana"]
newlist = []

for x in sehir:
    if "a" in x: 
        newlist.append(x)
print(newlist)

thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}

print(thisdict)


cars = {
    "araba1" : {
        "marka" : "toyota",
        "year" : 2000
    },
    "araba2" : {
        "marka": "ford",
        "year" : 2001
    },
    "araba3" : { 
        "marka" : "bmw",
        "year" : 2002
    },
}
print(cars)



def merhaba():
    global b 
    b = "harika"
merhaba()
print("Python" + b)

ilkliste = ["elma", "armut", "muz", "karpuz"]
print(ilkliste)
print(ilkliste[:2])
print(ilkliste[1])
print(ilkliste[0])
print(ilkliste[2])


ilkliste = ["elma", "armut", "muz", "karpuz"]
print(ilkliste[:2])
print(ilkliste[:3])
print(ilkliste[1])
print(ilkliste[2])

