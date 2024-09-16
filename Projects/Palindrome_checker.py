



def palindrome_kontrol(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

input_string = input("Enter a string: ")

if palindrome_kontrol(input_string):
    print(f"{input_string} bu bir palindromedur")
else:
    print(f"{input_string} bur bir palindrome degildir")
