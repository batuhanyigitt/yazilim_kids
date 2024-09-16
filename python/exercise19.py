import random 

selamlama = ["selam", "merhaba", "hosgeldin", "naber"]
kullanici_selam = ["selamlar", "hosbulduk", "nasilsin"]

sorular = ["Neler yapiyorsun?", "ne yaptin?", "iyi misin?"]
kullanici_sorular = ["iyiyim", "tesekkurler", "iyi, sen?"]


def chatbot_cevap(input_text):
    input_text = input_text.lower()
    
    for selam in selamlama:
        if selam in input_text:
            return random.choice(kullanici_selam)
        
    for soru in sorular:
        if soru in input_text:
            return random.choice(kullanici_sorular)
    return "Anlamadim"

print("Merhba, Nasil yardimci olabilirim? (cikis yapmak icin 'q' yazin)")
while True:
    user_input = input("Kullanici: ")
    if user_input.lower() == "q":
        print("Gorusmek uzere")
    cevap = chatbot_cevap(user_input)
    print("Chatbot:", cevap)
        
        