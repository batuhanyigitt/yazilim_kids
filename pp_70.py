def most_freq_character(sentence):
    characters_freq = {}
    for char in sentence:
        if char not in " ,.":
            characters_freq[char] = characters_freq.get(char, 0) + 1
    
    sorted_characters_freq = sorted(characters_freq.items(), key=lambda x: x[1], reverse=True)
    
    return sorted_characters_freq

sentence = "The robbed that smiles, steals something from the thief."
print(most_freq_character(sentence))
