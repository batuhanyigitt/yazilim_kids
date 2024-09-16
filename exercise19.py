import random

selamlama = ["selam", "merhaba", "hosgeldin", "naber"]
kullanici_selam = ["selamlar", "hosbulduk", "nasilsin"]

sorular = ["Neler yapiyorsun?", "ne yaptin?", "iyi misin?"]
kullanici_sorular = ["iyiyim", "tesekkurler", "iyi, sen?"]

karsilikli_sorular = ["Seninle sohbet etmek ne kadar güzel!", "Sence insanlar neden var?", "En sevdiğin renk nedir?"]
kullanici_karsilikli_sorular = ["Teşekkür ederim!", "Belki de insanlar bir anlam arıyorlar.", "Ben renkleri hissetmiyorum ama mavi güzel gibi geliyor."]

def get_weather(city):
    return f"Hava durumu şu anda güneşli {city}!"

def chatbot_cevap(input_text):
    input_text = input_text.lower()

    for selam in selamlama:
        if selam in input_text:
            return random.choice(kullanici_selam)

    for soru in sorular:
        if soru in input_text:
            return random.choice(kullanici_sorular)

    for karsilikli_soru in karsilikli_sorular:
        if karsilikli_soru in input_text:
            return random.choice(kullanici_karsilikli_sorular)

    if "hava durumu" in input_text:
        city_index = input_text.find("hava durumu") + len("hava durumu") + 1
        city = input_text[city_index:].strip()
        return get_weather(city)

    if "senin adın ne" in input_text:
        return "Ben bir chatbot'um, beni ChatGPT olarak adlandırabilirsin."

    return "Anlamadim"

print("Merhaba, Nasıl yardımcı olabilirim? (Çıkış yapmak için 'q' yazın)")
while True:
    user_input = input("Kullanıcı: ")
    if user_input.lower() == "q":
        print("Görüşmek üzere!")
        break
    
cevap = chatbot_cevap(user_input)
print("Chatbot:", cevap)


