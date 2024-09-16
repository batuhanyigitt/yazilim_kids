def remove_punctuation(text: str, remove_space: bool = False) -> str:

    import string
    punct = string.punctuation
    

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

my_str = "Wow! That's amazing. How did you do it? I'm so impressed. You're awesome, brilliant, and talented. Congratulations! Well done. Bravo!"

no_punct = ""
for char in my_str:
   if char not in punctuations:
       no_punct = no_punct + char

print(no_punct)
