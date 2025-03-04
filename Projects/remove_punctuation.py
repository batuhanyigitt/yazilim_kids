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