'''
Exercise 90, file pp_90.py
Write a program that will check if a word/sentence is a palindrome or not.
Remove punctuations and spaces
Use iterative way (loop) to check if palindrome

These are palindromes, test with them:
Dad 
Evil olive.
Never odd or even.
Amore, Roma.

Not palindromes:
test
ad
a
'''


def is_palindrome(text: str) -> bool:
    '''
    Function checks if any text is palindrome or not

    Parameters:
        text: any text
    Returns:
        True: if text is palindrome
        False: if text is not a palindrome
    '''
    # your code below
    
    

    text = ''.join(e for e in text if e.isalnum())

    text = text.lower()

    left = 0
    right = len(text) - 1

    while left < right:
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1
    return True

print(is_palindrome('Dad')) # True
print(is_palindrome('Evil olive.')) # True
print(is_palindrome('Never odd or even.')) # True
print(is_palindrome('Amore, Roma.')) # True
print(is_palindrome('test')) # False
print(is_palindrome('ad')) # True
print(is_palindrome('a')) # True
print(is_palindrome("'''")) # True 
