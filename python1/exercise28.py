import random

def guess_number():
    secret_number = random.randint(1, 10)
    attempts = 3
    
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 10.")

    while True:
        try:
            user_guess = int(input("Enter your guess (1-10): "))
            attempts += 1

            if user_guess < 1 or user_guess > 10:
                print("Please enter a valid number between 1 and 10.")
            elif user_guess < secret_number:
                print("Too low. Try again.")
            elif user_guess > secret_number:
                print("Too high. Try again.")
            else:
                print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

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