'''
sifre = "merhaba"
giris_hakki = 3
hak = 0
while hak < giris_hakki:
    user_input = input("Sifrenizi giriniz: ")
    if user_input == sifre:
        print("Dogrulandi! ")
        break 
    else: 
        print("Yanlis sifre")
        hak += 1
if hak == giris_hakki: 
    print("Erisim gecersiz. ")




sifre = "merhaba"
giris_hakki = 3
hak = 0

while hak < giris_hakki:
    user_input = input(f"Sifrenizi giriniz ({giris_hakki - hak} hak kaldı): ")
    if user_input == sifre:
        print("Doğrulandı!")
        break
    else:
        print("Yanlış şifre")
        hak += 1

if hak == giris_hakki:
    print("Erişim geçersiz.")

'''

import time 

while True: 
    user_input = input("Lutfen 'bip bip' yaziniz: ")
    if user_input.lower() == "bip bip":
        
        
        time.sleep(3)
        print("bip bip")
        break
    else: 
        print("Lutfen 'bip bip' yaziniz: ")
        
        
        
        


user_database = {
    "user1": "sifre123", 
    "user2": "sifre",
}
current_user = None 
def login(username, password):
    global current_user
    if username in user_database and user_database[username] == password:
        current_user = username
        print(f"Hosgeldin, {username}")
    else: 
        print("Giris basarisiz.")
def logout():
    global current_user
    if current_user:
        print(f"Goodbye, {current_user}!")
        current_user = None
    else:
        print("No user is currently logged in.")
def main():
    while True: 
        print("\nMenu: ")
        print("1. Login")
        print("2. Logout")
        print("3. Exit")
        choice = input("Seceneklerden birini secin (1/2/3): ")
        if choice == '1':
            if current_user: 
                print(f"Zaten giris yaptiniz {current_user}, oncelikle cikis yapin")
                continue
            username = input("Enter username: ")
            password = input("Enter password: ")
            login(username, password)
        elif choice == '2':
            logout()
        elif choice == '3':
            if current_user: 
                print("Oncelikle cikis yapman gerekiyor. ")
            else: 
                print("Program kapatiliyor")
                break 
        else: 
            print("yanlis bir sey yazdiniz bir daha yaziniz")
if __name__ == '__main__':
    main()
    
    
    
    
    





while True: 
    user_input = input("cikis yapmak icin 'cikis' yaz: ")
    if user_input == 'cikis':
        break
    
'''

import time

while True:
    user_input = input("Type 'bip bip': ")
    if user_input.lower() == "bip bip":
        print("bip bip")
        for i in range(3, 0, -1):
            print("Continuing in {} seconds...".format(i))
            time.sleep(1)
        break
    else:
        print("Please type 'bip bip'")


import time

while True:
    user_input = input("Lütfen 'bip bip' yazınız: ")
    if user_input.lower() == "bip bip":
        print("Doğrulandı! 3 saniye içinde 'bip bip' yazdırılacak...")
        
        for i in range(3, 0, -1):  # Countdown from 3 to 1
            print(f"{i}...")
            time.sleep(1)
        
        print("bip bip")
        break
    else:
        print("Yanlış giriş! Lütfen 'bip bip' yazınız.")





import time

while True:
    user_input = input("Type 'bip bip': ")
    if user_input.lower() == "bip bip":
        print("bip bip")
        time.sleep(3)  # Pause for 3 seconds
        break
    else:
        print("Please type 'bip bip'")


n = 5 
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "*" * (2 * i -1))


password = "sifre"
max_attempts = 3
attempts = 0

while attempts < max_attempts:
    user_input = input("Sifrenizi girin: ")
    if user_input == password:
        print("Dogrulandi!")
        break
    else:
        print("Gecersiz Sifre")
        attempts += 1
if attempts == max_attempts:
    print("Erisim gecersiz. ")
    '''
    
    

while True:
    user_input = input("Type 'exit' to quit: ")
    if user_input == 'exit':
        break




while True:
    user_input = input("Type 'exit' to quit: ")
    if user_input == 'exit':
        break



   
n = 5
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))





'''
for kalem in range(1, 11):
    print(kalem)
    
for elma in range(0, 21, 2):
    print(elma)
    
for armut in range(1, 22, 2):
    print(armut)
''' 
    
karpuz = 1
while karpuz <= 5:
    print("*" * karpuz)
    karpuz += 1
    
    
while True: 
    kullanici_input = input("Cikis yapmak icin 'cikis' yaz")
    if kullanici_input == 'cikis':
        break
    

    
    

for kalem in range(1, 11):
    print(kalem)
    
for k in range(1, 21):
    print(k)
    
        
for a in range(0, 21, 2):
    print(a)
        

for b in range(1, 20, 2):
    print(b)
    
for a in range(5, 0, -1):
    print("*" * a)
    
    
    
    
'''
satir = 1
while satir <= 5:
    print("*" * satir)
    satir += 1

for kalem in range(1, 11):
    print(kalem)
    
for k in range(1, 20):
    print(k)
    
for a in range(0, 20, 2):
    print(a)
    
for b in range(3, 30, 3):
    print(b)

for o in range(10, 0, -1):
    print(o)   

fil = 5
i = 1

while i <= fil:
    if i == 1 or i == fil:
        print("*"*fil)
    else:
        print("*"+ " " * (fil -2) + "*")
    i += 1 
def selam():
    print("Merhaba")
selam()
'''
'''
kullanci_input = ""
while kullanci_input != "q":
    kullanci_input = input("Cikis yapmak icin 'q' tusuna basiniz:")
    print("Kullanici input:", kullanci_input)
    
    basamak = 10
bosluk = basamak - 1 
i = 1

while i <= basamak:
    print(" "* bosluk + "*"*(2*i-1))
    bosluk -= 1
    i += 1 
    

def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

input_string = "racecar"
if is_palindrome(input_string):
    print(f"{input_string} is a palindrome.")
else:
    print(f"{input_string} is not a palindrome.")
    
    
'''



n = 5
factorial = 1
while n > 0:
    factorial *= n
    n -= 1
print(f"5! is {factorial}") 


n = 10
a, b = 0, 1
count = 0
while count < n:
    print(a, end=' ')
    a, b = b, a + b
    count += 1


while True:
    user_input = input("Type 'exit' to quit: ")
    if user_input == 'exit':
        break








user_database = {
    "user1": "password123",
    "user2": "mypassword",
}


current_user = None
def login(username, password):

    global current_user
    if username in user_database and user_database[username] == password:
        current_user = username
        print(f"Login successful! Welcome, {username}.")
    else:
        print("Login failed. Incorrect username or password.")

def logout():

    global current_user
    if current_user:
        print(f"Goodbye, {current_user}!")
        current_user = None
    else:
        print("No user is currently logged in.")

def main():

    while True:
        print("\nMenu:")
        print("1. Login")
        print("2. Logout")
        print("3. Exit")
        
        choice = input("Select an option (1/2/3): ")
        
        if choice == '1':
            if current_user:
                print(f"Already logged in as {current_user}. Please log out first.")
                continue
            username = input("Enter username: ")
            password = input("Enter password: ")
            login(username, password)
        elif choice == '2':
            logout()
        elif choice == '3':
            if current_user:
                print("You are currently logged in. Please log out before exiting.")
            else:
                print("Exiting the program.")
                break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()













password = "sifre"
max_attempts = 3
attempts = 0
while attempts < max_attempts:
    user_input = input("Sifrenizi girin: ")
    if user_input == password:
        print("Dogrulandi!")
        break
    else:
        print("Gecersiz sifre")
        attempts += 1
if attempts == max_attempts:
    print("Erisim gecersiz.")