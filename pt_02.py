import string
from collections import Counter

def remove_punctuation(text: str, remove_space: bool = False) -> str:
    '''
    Function removes punctuations !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ optionally it can remove spaces

    Parameters:
        text: any text
        remove_space: if True, spaces are removed, if False, spaces are not removed
    Returns:
        text without punctuation, optionally spaces
    '''
    if remove_space:
        text = text.replace(" ", "")
    translator = str.maketrans("", "", string.punctuation)
    return text.translate(translator)

def get_character_freq(sentence: str) -> list[tuple[str, int]]:
    '''
    Function returns list of characters together with its length

    Parameters:
        sentence: any text
    Returns:
        List of tuples
    '''
    sentence = remove_punctuation(sentence.lower(), remove_space=True)
    char_freq = Counter(sentence)
    return char_freq.most_common()

sentence = '''
 As fast as thou shalt wane so fast thou grow'st,
  In one of thine, from that which thou departest,
  And that fresh blood which youngly thou bestow'st,
  Thou mayst call thine, when thou from youth convertest,
  Herein lives wisdom, beauty, and increase,
  Without this folly, age, and cold decay,
  If all were minded so, the times should cease,
  And threescore year would make the world away:
  Let those whom nature hath not made for store,
  Harsh, featureless, and rude, barrenly perish:
  Look whom she best endowed, she gave thee more;
  Which bounteous gift thou shouldst in bounty cherish:
    She carved thee for her seal, and meant thereby,
    Thou shouldst print more, not let that copy die.
'''

print(get_character_freq(sentence))
