import random 

def play_number_matching():
    print("welcome")
    
    while True:
        number_list = random.sample(range(1, 11), 5)
        random.shuffle(number_list)
        print(f"sayilar: {number_list}")
        correct_positions = [0] * 5
        for i in range(5):
            while True:
                try: 
                    guess = int(input(f"dogru hizlamayi gir {number_list[i]}(1-5):"))
                    if guess < 0 or guess > 4 or correct_positions[guess]!=0:
                        print("gecersiz tahmin, bir daha dene")
                    else: 
                        correct_positions[guess] = number_list[i]
                        break
                except ValueError: 
                    print("gecersiz tahmin. bir daha dene (1-5).")
                    