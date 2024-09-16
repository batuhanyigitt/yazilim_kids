'''

print("ilk mesaj")

deneme = 5
print(deneme)

selam = "merhaba"
print(selam)




ilkliste = ["elma", "armut", "muz", "karpuz"]
print(ilkliste)
print(ilkliste[0])
print(ilkliste[1])
print(ilkliste[:2])
print(ilkliste[2:])

'''




def merhaba():
    global b
    b = "harika"
merhaba()
print("Python" + b)




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
