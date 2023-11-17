from translate import Translator

def get_translation(input_text, source_lang, target_lang):
    translator = Translator(from_lang=source_lang, to_lang=target_lang)
    translation = translator.translate(input_text)
    return translation
def main():
    print("Translation Tool")

    while True:
        print("\nSelect an option:")
        print("1. Translate from English to German")
        print("2. Translate from English to French")
        print("3. Translate from English to Spanish")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "4":
            print("Goodbye!")
            break

        if choice not in ["1", "2", "3"]:
            print("Invalid choice. Please select a valid option.")
            continue

        source_lang = "en"
        target_lang = "de" if choice == "1" else ("fr" if choice == "2" else "es")

        input_text = input("Enter the text to translate: ")

        if not input_text:
            print("No text provided for translation.")
            continue

        translation = get_translation(input_text, source_lang, target_lang)
        print(f"Translation ({target_lang}): {translation}")

if __name__ == "__main__":
    main()
