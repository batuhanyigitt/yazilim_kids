



def most_freq_character(sentence):
    char_count = {}

    for char in sentence:
        if char != ' ':
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

    sorted_characters_freq = sorted(char_count.items(), key=lambda x: x[1], reverse=True)

    return sorted_characters_freq

sentence = "The robbed that smiles, steals something from the thief."
print(most_freq_character(sentence))

