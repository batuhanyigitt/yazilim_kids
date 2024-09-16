import random

def guess_number():
    secret_number = random.randint(1, 10)
    attempts = 3

    print("SAYI TAHMIN OYUNUNA HOSGELDINIZ")
    print("LUTFEN TAHMIN 1-10 ARASINDA BIR SAYI TAHMIN EDIN")

    while attempts > 0:
        try:
            print(f"Kalan deneme hakkiniz: {attempts}")
            user_guess = int(input("Tahmin giriniz (1-10): "))

            if user_guess < 1 or user_guess > 10:
                print("Lutfen gecerli bir tahmin giriniz.")
            elif user_guess < secret_number:
                print("Kucuk tahmin yaptiniz, arttirin.")
                attempts -= 1
            elif user_guess > secret_number:
                print("Buyuk tahmin yaptiniz, biraz dus.")
                attempts -= 1
            else:
                print(f"Tebrikler dogru bildiniz! {secret_number} sayisini bildiniz.")
                break

            if attempts == 0:
                print(f"Uzgunum, tahmin hakkiniz bitti. Gizli sayi {secret_number} idi.")
        except ValueError:
            print("Hatali giris yaptiniz, lutfen sayi girin.")

if __name__ == "__main__":
    guess_number()

    
    










import string 
from collections import Counter

def remove_punctuation(text: str, remove_space: bool = False) -> str:
    if remove_space:
        text = text.replace(" ", "")
    translator = str.maketrans("", "", string.punctuation)
    return text.translate(translator)

def get_character(sentence: str) -> list[tuple[str, int]]:
    sentence = remove_punctuation(sentence.lower(), remove_space=True)
    char_freq = Counter(sentence)
    return char_freq.most_common()

sentence = '''
Lorem ipsum dolor sit amet, 
consectetur adipiscing elit, 
sed do eiusmod tempor incididunt 
ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud 
exercitation ullamco labosris nisi ut 
aliquip ex ea commodo consequat. 
Duis aute irure dolor in reprehenderit 
in voluptate velit esse cillum dolore 
eu fugiat nulla pariatur. Excepteur sint 
occaecat cupidatat non 5464 proident, sunt 
in culpa qui officia deserunt mollit 
anim id est laborum.
'''
print(get_character(sentence))