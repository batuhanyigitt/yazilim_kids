'''

def not_getir(score):
    if score >= 90:
        return "Pekiyi"
    elif score >= 80:
        return "iyi"
    elif score >= 70:
        return "ortta"
    elif score >= 60:
        return "gecer"
    else: 
        return "kaldi"
    
user_score = int(input("notunuzu giriniz: "))

if user_score > 100:
    print("abartma, gecerli not gir (0 - 100)")
else:
    grade = not_getir(user_score)
    print(f"Notunuz: {grade}")


num = int(input("sayi giriniz: "))
if num % 2 == 0:
    if num % 3 == 0:
        print("sayi hem 2'ye hem de 3'de tam bolunur")
    else:
        print("sayi 2'ye tam bolunur ama 3'e bolunmez")
elif num % 3 == 0:
    print("sayi 3'e tam bolunur, fakat 2'ye bolunemz")
else: 
    print("hicbirine bolunmez.")
'''
 
    
    
    
def maas_hesapla(saatlik_ucret, calisma_suresi):
    return saatlik_ucret * calisma_suresi


saatlik_ucret = float(input("saatlik ucreti giriniz: "))
calisma_suresi = float(input("aylik calisma saatinizi giriniz: "))

aylik_maas = maas_hesapla(saatlik_ucret, calisma_suresi)
print(f"aylik maasiniz: {aylik_maas}")





def not_getir(score):
    if score >= 90:
        return "Pekiyi"
    elif score >= 80:
        return "Iyi"
    elif score >= 70:
        return "Orta"
    elif score >= 60:
        return "Gecer"
    else: 
        return "Kaldi"

user_score = int(input("Notunuzu giriniz: "))
grade = not_getir(user_score)
print(f"Notunuz: {grade}")






import random
quiz_questions = [
    {
        "question": "What is the capital of France?",
        "options": ["London", "Berlin", "Paris", "Madrid"],
        "correct_answer": "Paris"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Mars", "Venus", "Jupiter", "Saturn"],
        "correct_answer": "Mars"
    },
    {
        "question": "What is the largest mammal in the world?",
         "options": ["Elephant", "Giraffe", "Blue Whale", "Lion"],
        "correct_answer": "Blue Whale"
    }
]

def ask_question(question_data):
    print(question_data["question"])
    for i, option in enumerate(question_data["options"],1):
        print(f"{i}. {option}")
        
    while True:
        try:
            user_choice = int(input("Cevap numarasini giriniz: "))
            if 1 <= user_choice <= len(question_data["options"]):
                return question_data["options"][user_choice - 1] 
            else:
                print("Yanlis bir islem yaptiniz. Bir daha deneyin.")
        except ValueError:
            print("Yanlis bir islem yaptiniz.")
            

def quiz_game():
    score = 0
    random.shuffle(quiz_questions)
            
    print("Welcome to the Quiz Game!\n")
            
    for question_data in quiz_questions:
        user_answer = ask_question(question_data)
        if user_answer == question_data["correct_answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {question_data['correct_answer']}\n")
                
    print(f"You scored {score} out of {len(quiz_questions)}.")
            
if __name__ == "__main__":
    quiz_game()
    
    
    
    
    def not_getir(score):
    if score >= 90:
        return "PEKIYI"
    elif score >= 80:
        return "IYI"
    elif score >= 70:
        return "ORTA"
    elif score >= 60:
        return "IDARE EDER"
    elif score >= 50:
        return "BERBAT"
    elif score >= 40:
        return "COK KOTU"
    elif score >= 30:
        return "GELISTIRILMELI"
    elif score >= 20:
        return "COK CALISMALISIN"
    elif score >= 10:
        return "BERBATIN BERBATI"
    elif score >= 0:
        return "IDARE ETMEZ"
    
ogrenci_score = int(input("OGRENCININ NOTUNU GIRINIZ: "))
notlar = not_getir(ogrenci_score)
print(f"OGRENCININ NOTU: {notlar}")
    
    
    
    
    
    
    
    
    
    
    
    
def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

user_score = int(input("Enter your score: "))
grade = get_grade(user_score)
print(f"Your grade is: {grade}")




num = int(input("sayi giriniz:"))
if num%2 == 0:
    if num%3 == 0:
        print("sayi 2'ye ve 3'e tam bolunur")
    else:
        print("sayi 2'ye tam bolunur, fakat 3'e bolunmez")
else:
    if num%3 == 0:
        print("sayi 3'e tam bolunur, fakat 2'ye bolunmez")
    else: 
        print("hicbirine tam bolunmez")
        
        


        num = int(input("sayi giriniz: "))
        mod = num % 2
        if mod > 0:
            print("sayi tek.")
        else: 
            print("sayi cift.")
            

def maas_hesapla(saatlik_ucret, calisma_suresi):
    return saatlik_ucret * calisma_suresi

saatlik_ucret = float(input("Saatlik ücreti giriniz (TL/saat): "))
calisma_suresi = float(input("Aylık çalışma saatinizi giriniz: "))

aylik_maas = maas_hesapla(saatlik_ucret, calisma_suresi)

print(f"Aylık maaşınız: {aylik_maas} TL")






num = int(input("Sayıyı giriniz: "))

if num % 2 == 0:
    if num % 3 == 0:
        if num % 4 == 0:
            print("Sayı 2'ye, 3'e ve 4'e tam bölünür.")
        else:
            print("Sayı 2'ye ve 3'e tam bölünür ama 4'e tam bölünmez.")
    else:
        if num % 4 == 0:
            print("Sayı 2'ye ve 4'e tam bölünür ama 3'e tam bölünmez.")
        else:
            print("Sayı sadece 2'ye tam bölünür.")
else:
    if num % 3 == 0:
        if num % 4 == 0:
            print("Sayı 3'e ve 4'e tam bölünür ama 2'ye tam bölünmez.")
        else:
            print("Sayı sadece 3'e tam bölünür.")
    else:
        if num % 4 == 0:
            print("Sayı sadece 4'e tam bölünür.")
        else:
            print("Sayı hiçbirine tam olarak bölünmez.")







def check_divisibility(num, divisors):
    divisible_by = [d for d in divisors if num % d == 0]

    if num == 0:
        return "0 her sayıya tam bölünür."
    elif divisible_by:
        return f"{num} sayısı {', '.join(map(str, divisible_by))}'e tam bölünür."
    else:
        return f"{num} sayısı bu sayılardan hiçbirine tam bölünmez: {', '.join(map(str, divisors))}."


def main():
    divisors = list(map(int, input("Kontrol edilecek bölenleri girin (virgülle ayırın): ").split(',')))
    numbers = list(map(int, input("Kontrol edilecek sayıları girin (virgülle ayırın): ").split(',')))

    for num in numbers:
        result = check_divisibility(num, divisors)
        print(result)

if __name__ == "__main__":
    main()






num = int(input("Sayı giriniz: "))
if num % 2 == 0:
    if num % 3 == 0:
        print("Sayı hem 2'ye hem de 3'e tam bölünür.")
    else:
        print("Sayı 2'ye tam bölünür, fakat 3'e bölünmez.")
elif num % 3 == 0:
    print("Sayı 3'e tam bölünür, fakat 2'ye bölünmez.")
else:
    print("Hiçbirine tam bölünmez.")






if user_score > 100:
    print("Lütfen geçerli bir not giriniz (0-100 arası).")


            import random

            # List of words for the game
            word_list = ["apple", "banana", "cherry", "grape", "orange", "strawberry"]
            
            # Select a random word from the list
            secret_word = random.choice(word_list)
            
            # Initialize variables
            guessed_letters = []
            max_attempts = 6
            
            def display_word(word, guessed_letters):
                display = ""
                for letter in word:
                    if letter in guessed_letters:
                        display += letter
                    else:
                        display += "_"
                return display
            
            print("Welcome to Hangman!")
            print(f"Try to guess the word. You have {max_attempts} attempts.")
            
            while max_attempts > 0:
                print("\n" + display_word(secret_word, guessed_letters))
                guess = input("Guess a letter: ").lower()
                
                if len(guess) != 1 or not guess.isalpha():
                    print("Please enter a single letter.")
                    continue
                
                if guess in guessed_letters:
                    print("You've already guessed that letter.")
                    continue
                
                guessed_letters.append(guess)
                
                if guess in secret_word:
                    print("Good guess!")
                else:
                    max_attempts -= 1
                    print(f"Wrong guess! You have {max_attempts} attempts left.")
                
                if "_" not in display_word(secret_word, guessed_letters):
                    print(f"Congratulations! You guessed the word '{secret_word}' correctly!")
                    break
            
            if max_attempts == 0:
                print(f"Sorry, you've used up all your attempts. The word was '{secret_word}'. Better luck next time!")
            
            
            
            import random
            quiz_questions = [
                {
                    "question": "What is the capital of France?",
                    "options": ["London", "Berlin", "Paris", "Madrid"],
                    "correct_answer": "Paris"
                },
                {
                    "question": "Which planet is known as the Red Planet?",
                    "options": ["Mars", "Venus", "Jupiter", "Saturn"],
                    "correct_answer": "Mars"
                },
                {
                    "question": "What is the largest mammal in the world?",
                    "options": ["Elephant", "Giraffe", "Blue Whale", "Lion"],
                    "correct_answer": "Blue Whale"
                }
            ]
            def ask_question(question_data):
                print(question_data["question"])
                for i, option in enumerate(question_data["options"], 1):
                    print(f"{i}. {option}")
                
                while True:
                    try:
                        user_choice = int(input("Enter the number of your answer: "))
                        if 1 <= user_choice <= len(question_data["options"]):
                            return question_data["options"][user_choice - 1]
                        else:
                            print("Invalid choice. Please choose a valid option.")
                    except ValueError:
                        print("Invalid input. Please enter a number.")
            
            def quiz_game():
                score = 0
                random.shuffle(quiz_questions)
            
                print("Welcome to the Quiz Game!\n")
            
                for question_data in quiz_questions:
                    user_answer = ask_question(question_data)
                    if user_answer == question_data["correct_answer"]:
                        print("Correct!\n")
                        score += 1
                    else:
                        print(f"Wrong! The correct answer is: {question_data['correct_answer']}\n")
                
                print(f"You scored {score} out of {len(quiz_questions)}.")
            
            if __name__ == "__main__":
                quiz_game()
            
            
            
            ''''
            from datetime import datetime
            now = datetime.now()
            year = now.strftime("%Y")
            month = now.strftime("%m")
            
            byear = int(input("Dogum yilinizi giriniz:"))
            bmonth = int(input("dogum ayinizi giriniz: "))
            bname = str(input("Adinizi giriniz:"))
            year = int(year)
            month = int(month)
            
            if(byear < year):
                if(bmonth < month):
                    x = year - byear
                    y = month - bmonth 
                    z = bname 
                    print(f"ismin {z} ve yasin {x} ve ayliksin {y}")
                else: 
                    x = (year - byear) - 1 
                    y = (12 - bmonth) + month
                    z = bname 
                    print(f"ismin {z} ve yasin {x} ve de ayliksin {y}")
            else:
                print("yanlis bilgi girdiniz")
            
            
            def is_palindrome(s):
                s = s.lower().replace(" ", "")
                return s == s[::-1]
            
            input_string = "madam"
            if is_palindrome(input_string):
                print(f"{input_string} bir palindromdur.")
            else:
                print(f"{input_string} bir palindrom degildir.")
            '''
            
            def is_prime(n):
                if n <= 1:
                    return False
                if n <= 3:
                    return True
                if n % 2 == 0 or n % 3 == 0:
                    return False
                i = 5
                while i * i <= n:
                    if n % i == 0 or n % (i + 2) == 0:
                        return False
                    i += 6
                return True
            
            number = 17
            if is_prime(number):
                print(f"{number} is a prime number.")
            else:
                print(f"{number} is not a prime number.")
                
                
                '''
            def bubble_sort(arr):
                n = len(arr)
                for i in range(n):
                    for j in range(0, n - i - 1):
                        if arr[j] > arr[j+1]:
                            arr[j], arr[j+1] = arr[j+1], arr[j]
                
            my_list = [64, 39, 25, 12, 22, 11, 90]
            bubble_sort(my_list)
            print("Siralanan arrayler bunlar:", my_list)  
            
            
            
            
            def is_palindrome(s):
                s = s.lower().replace(" ", "")
                return s == s[::-1]
            
            input_string = "racecar"
            if is_palindrome(input_string):
                print(f"{input_string} is a palindrome.")
            else:
                print(f"{input_string} is not a palindrome.")
            '''
            
            
            def is_prime(n):
                if n <= 1:
                    return False
                if n <= 3:
                    return True
                if n % 2 == 0 or n % 3 == 0:
                    return False
                i = 5
                while i * i <= n:
                    if n % i == 0 or n % (i + 2) == 0:
                        return False
                    i += 6
                return True
            
            number = 17
            if is_prime(number):
                print(f"{number} is a prime number.")
            else:
                print(f"{number} is not a prime number.")
                
                
            import random
            def play_rock_paper_scissors():
                choices = ["rock", "paper", "scissors"]
                user_choice = input("Choose rock, paper, or scissors: ").lower()
                
                if user_choice not in choices:
                    print("Invalid choice. Please choose rock, paper, or scissors.")
                    return
                
                computer_choice = random.choice(choices)
                print(f"Computer chose: {computer_choice}")
                
                if user_choice == computer_choice:
                    print("It's a tie!")
                elif user_choice == "rock":
                    if computer_choice == "paper":
                        print("Computer wins!")
                    else:
                        print("You win!")
                elif user_choice == "paper":
                    if computer_choice == "scissors":
                        print("Computer wins!")
                    else:
                        print("You win!")
                elif user_choice == "scissors":
                    if computer_choice == "rock":
                        print("Computer wins!")
                    else:
                        print("You win!")
            
            print("Welcome to Rock, Paper, Scissors!")
            play_rock_paper_scissors()










def check_divisibility(num, divisors):
    divisible_by = [d for d in divisors if num % d == 0]

    if num == 0:
        return "0 her sayıya tam bölünür."
    elif divisible_by:
        return f"{num} sayısı {', '.join(map(str, divisible_by))}'e tam bölünür."
    else:
        return f"{num} sayısı bu sayılardan hiçbirine tam bölünmez: {', '.join(map(str, divisors))}."


def main():
    divisors = list(map(int, input("Kontrol edilecek bölenleri girin (virgülle ayırın): ").split(',')))
    numbers = list(map(int, input("Kontrol edilecek sayıları girin (virgülle ayırın): ").split(',')))

    for num in numbers:
        result = check_divisibility(num, divisors)
        print(result)

if __name__ == "__main__":
    main()