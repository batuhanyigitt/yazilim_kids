


import re

def remove_punctuation(text, preserve_emoticons=True, preserve_contractions=True):
    punctuation_pattern = r'[,.;:!?]'

    emoticon_pattern = r'[:;=][)(/\[\]]|[*][\w-]*[*]'

    contraction_pattern = r"\b\w+(?:'\w+)?"

    text_without_punctuation = re.sub(punctuation_pattern, '', text)

    if not preserve_contractions:
        text_without_punctuation = re.sub(contraction_pattern, '', text_without_punctuation)

    if preserve_emoticons:
        emoticons = re.findall(emoticon_pattern, text)
        text_without_punctuation += ' '.join(emoticons)

    return text_without_punctuation

input_text = "Hello! How are you doing? I'm doing fine, thank you! :)"
text_without_punctuation = remove_punctuation(input_text)
print("Text without punctuation:")
print(text_without_punctuation)












import re

def remove_punctuation(text):

    punctuation_pattern = re.compile(r'[^\w\s]')


    text_without_punctuation = re.sub(punctuation_pattern, '', text)

    return text_without_punctuation


input_text = "Hello! How are you doing? I'm doing fine, thank you!"
text_without_punctuation = remove_punctuation(input_text)
print("Text without punctuation:")
print(text_without_punctuation)

