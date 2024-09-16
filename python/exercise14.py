'''
def ucgen_tanimlama(kenar1, kenar2, kenar3):
    if kenar1 == kenar2 == kenar3:
        return "Eskenar Ucgen"
    elif kenar1 == kenar2 or kenar1 == kenar3 or kenar2 == kenar3:
        return "Ikizkenar Ucgen"
    else: 
        return "Cesitkenar Ucgen"

kenar1 = float(input("1. Kenar: "))
kenar2 = float(input("2. Kenar: "))
kenar3 = float(input("3. Kenar: "))

ucgen_yazdirma = ucgen_tanimlama(kenar1, kenar2, kenar3)
print(f"Ucgenin cesidi: {ucgen_yazdirma}")

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
'''


def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

input_string = "racecar"
if is_palindrome(input_string):
    print(f"{input_string} is a palindrome.")
else:
    print(f"{input_string} is not a palindrome.")
    
    
    
    
    '''
def ucgen_tanimlama(kenar1, kenar2, kenar3):
    if kenar1 == kenar2 == kenar3:
        return "Eskenar Ucgen"
    elif kenar1 == kenar2 or kenar1 == kenar3 or kenar2 == kenar3:
        return "Ikizkenar Ucgen"
    else: 
        return "Cesitkenar Ucgen"

kenar1 = float(input("1. Kenar: "))
kenar2 = float(input("2. Kenar: "))
kenar3 = float(input("3. Kenar: "))

ucgen_yazdirma = ucgen_tanimlama(kenar1, kenar2, kenar3)
print(f"Ucgenin cesidi: {ucgen_yazdirma}")
'''

# Linear Search Algorithm
'''
def linear_search(arr, target):
    for index, element in enumerate(arr):
        if element == target:
            return index
    return -1

my_list = [2, 3, 5, 7, 11, 13 ,17, 19 ]
target_value = 19
result = linear_search(my_list, target_value)
print(f"Hedef degeri {target_value} bulundu ve indexi {result}" if result != -1 else "hedef degeri yok")
'''


