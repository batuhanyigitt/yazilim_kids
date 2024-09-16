import random 

selamlama = ["merhaba", "nasilsin", "bugun nasilsin"]
selamlama2 = ["merhaba", "iyi misin?", "nasil gidiyor?", "bugun nasilsin?"]

soru = ["ne yapiyorsun?", "nasil gidiyor?", "nasil yardimci olabilirim?", "sormak istedigin nedir?"]
soru2 = ["iyiyim, sen?", "tesekkurler", "iyi"]


def chatbot_cevap(input_text):
    input_text = input_text.lower()
    
    for selamla in selamlama:
        if selamla in input_text:
            return random.choice(selamlama2)
    
    for sor in soru:
        if sor in input_text:
            return random.choice(soru2)
    return "anlamadim"

print("Ben bir Chatbot'um. Hosgeldin! (Cikis yapmak icin 'bay' yazabilirsin)")
while True:
    user_input = input("Sen: ")
    if user_input.lower() == "bay":
        print("Chatbot: Sohbet botu kapaniyor")
        break
    cevap = chatbot_cevap(user_input)
    print("Chatbot:", cevap)
        