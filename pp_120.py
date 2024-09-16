import string

def remove_punctuation(text: str, remove_space: bool = False) -> str:
    '''
    Function removes punctuations !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ optionally it can remove spaces

    Parameters:
        text: any text
        remove_space: if True, spaces are removed, if False, spaces are not removed
    Returns:
        text without punctuation, optionally spaces
    '''
    translator = str.maketrans('', '', string.punctuation)
    if remove_space:
        return text.translate(translator).replace(" ", "")
    else:
        return text.translate(translator)

def is_palindrome(text: str) -> bool:
    '''
    Function checks if any text is a palindrome

    Parameters:
        text: any text
    Returns:
        True: if text is palindrome
        False: if text is not a palindrome
    '''
    if len(text) <= 1:
        return True
    else:
        return text[0] == text[-1] and is_palindrome(text[1:-1])
    
def print_palindrome_check(text: str) -> None:
    '''
    Function prints the message if text is palindrome or not

    Parameters:
        text: any text
    '''
    text = remove_punctuation(text, remove_space=True).lower()
    if is_palindrome(text):
        print(f"{text} is a palindrome!")
    else:
        print(f"{text} is not a palindrome.")
        
        
print_palindrome_check("Dad")
print_palindrome_check("Evil olive.")
print_palindrome_check("Never odd or even.")
print_palindrome_check("Amore, Roma.")
print_palindrome_check("test")
print_palindrome_check("ad")
print_palindrome_check("a")
