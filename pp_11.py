import re

def analyze_text(file_path, start_line):
    with open(file_path, 'r') as file:
        for _ in range(start_line - 1):
            next(file)

        words = []
        count = 0

        for line in file:
            matching_words = re.findall(r'\b[aeoiuy]\w{4}[bcdfghjklmnpqrstvwz]\b', line)
            words.extend(matching_words)
            count += len(matching_words)

    print("Results:")
    print(words)
    print("The amount of words is", count)

file_path = input("Enter the text filepath: ")
start_line = int(input("Enter the line number for start: "))

analyze_text(file_path, start_line)
