from translate import Translator

def translate_text(text, target_language):
    translator = Translator(to_lang=target_language)
    translation = translator.translate(text)
    return translation 

def main():
    print("CEVIRI UYGULAMASINA HOSGELDINIZ")
    source_language = "en"
    
    while True: 
        text = input(f"cevirmek istediginiz dili giriniz {source_language}. Cikis yapmak icin 'q' ya tiklayin:")
        if text.lower() == 'q':
            break    
        target_language = input("Lutfen cevrilmesini istediginiz dilin kodunu giriniz. Ornegin: tr, de, fr, es, it")
        translated_text = translate_text(text, target_language)
        print(f"Ceviri: {translated_text}")

if __name__ == "__main__":
    main()