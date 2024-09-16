def get_text(file_path: str) -> str:
    try:
        with open(file_path, 'r') as file:
            text = file.read()
        return text
    except FileNotFoundError:
        print("File not found.")
        return ""

def remove_punctuation(word: str, remove_space: bool = False) -> str:
    import string
    punctuation = string.punctuation
    if remove_space:
        punctuation = punctuation.replace(" ", "")
    return word.translate(str.maketrans('', '', punctuation))

def map_longest(text: str) -> list[tuple[str, int]]:
    words = text.split()
    word_lengths = map(lambda word: (word, len(word)), words)
    sorted_words = sorted(word_lengths, key=lambda x: x[1], reverse=True)
    return sorted_words

def print_word_length_list(word_l: list[tuple[str, int]], number: int) -> None:
    if len(word_l) < number:
        number = len(word_l)
    for i in range(number):
        print(f"The longest word in the file is '{word_l[i][0]}' with a length of {word_l[i][1]} characters")

file_path = input("Enter the file path: ")
text = get_text(file_path)
if text:
    word_list = map_longest(text)
    print_word_length_list(word_list, 10)
