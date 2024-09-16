import sys
import string


def get_text(file_path: str) -> str:
    '''
    Function opens the text file and returns its content

    Parameters:
        file_path: path to your text file
    Returns:
        text
    '''
    try:
        with open(file_path, 'r') as f:
            text = f.read()
            return text
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)


def remove_punctuation(word: str) -> str:
    '''
    Function removes punctuation from the given string

    Parameters:
        word: any string with or without the punctuation
    Returns:
        string without punctuation
    '''
    return ''.join([c for c in word if c not in string.punctuation])


def map_longest(text: str) -> tuple:
    '''
    Function returns the longest word in the text and its length

    Parameters:
        text: any text

    Returns:
        tuple: a tuple containing the longest word and its length
    '''
    words = text.split()
    longest_word = max(words, key=lambda w: len(w))
    return (longest_word, len(longest_word))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Error: Please provide the file path as a command-line argument.")
        sys.exit(1)

    file_path = sys.argv[1]
    text = get_text(file_path)

    # With punctuation removal
    text_without_punctuation = remove_punctuation(text)
    longest_word, longest_word_length = map_longest(text_without_punctuation)
    print(f"The longest word in the file '{file_path}' is '{longest_word}' with the length of {longest_word_length} characters (after punctuation removal).")

    # Without punctuation removal
    longest_word, longest_word_length = map_longest(text)
    print(f"The longest word in the file '{file_path}' is '{longest_word}' with the length of {longest_word_length} characters (without punctuation removal).")
