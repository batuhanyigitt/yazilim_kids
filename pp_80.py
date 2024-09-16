shakespeare = 'When forty winters shall besiege thy brow, And dig deep trenches in thy beautys field, ....'

def get_longest_word(text: str) -> tuple[str, int]:
    '''
    Function returns the longest word together with its length

    Parameters:
        text: any text
    Returns:

    Exemplary result:
    ('trenches',8)
    '''
    text = text.replace(',', '').replace('.', '')
    words = text.split()
    word_lengths = {word: len(word) for word in words}
    sorted_word_lengths = sorted(word_lengths.items(), key=lambda x: x[1], reverse=True)
    longest_word, length = sorted_word_lengths[0]
    return longest_word, length

longest_word, length = get_longest_word(shakespeare)
print(f"The longest word is '{longest_word}' with the length {length} characters.")
