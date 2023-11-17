from translate import Translator

def translate_text(text, target_language):
    translator = Translator(to_lang=target_language)
    translation = translator.translate(text)
    return translation

def main():
    print("Ceviri botuna hosgeldiniz!")
    source_language = "en"
    
    while True: 
        text = input(f"Cevirmek istediginiz metni giriniz {source_language} cikis yapmak icin 'q' a basiniz:")
        if text.lower() == 'q':
            break
        target_language = input("hedef dil kodunu giriniz 'ornegin: tr, de, fr, es, it, pt, ru, ar, zh, ja, ko'")
        translated_text = translate_text(text, target_language)
        print(f"Translation: {translated_text}")

if __name__ == "__main__":
    main()


