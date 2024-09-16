import re
import sys


def get_text(file_path: str, start_line: int) -> str:
    try:
        with open(file_path, 'r') as file:
            for _ in range(start_line - 1):
                file.readline()
            text = file.read()
        return text
    except FileNotFoundError:
        print("File not found.")
        return ""


def find_5_character_words(text: str) -> list[str]:
    pattern = r'\b\w{5}\b'
    matches = re.findall(pattern, text)
    return matches


def main():
    file_path = input("Enter the file path: ")
    start_line = int(input("Enter the line number to start analysis from: "))

    text = get_text(file_path, start_line)
    if text:
        words = find_5_character_words(text)
        if words:
            for word in words:
                print(f"Found 5-character word: {word}")
        else:
            print("No 5-character words found.")


if __name__ == "__main__":
    main()
