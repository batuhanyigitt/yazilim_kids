

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





def cube(number):
    return number ** 3

num = int(input("Enter a number: "))
result = cube(num)
print(f"The cube of {num} is {result}")


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





def cube(number):
    return number ** 3

num = int(input("Enter a number: "))
result = cube(num)
print(f"The cube of {num} is {result}")
