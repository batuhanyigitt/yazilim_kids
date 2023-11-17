# List of words for the game
word_list = ["python", "programming", "challenge", "computer", "keyboard", "algorithm"]

# Function to scramble a word (without randomization)
def scramble_word(word):
    # Simply reverse the word
    return word[::-1]

# Function to play Word Scramble
def word_scramble():
    original_word = "programming"  # Manually choose a word from the list
    scrambled_word = scramble_word(original_word)

    print("Welcome to Word Scramble!")
    print(f"Here's a scrambled word: {scrambled_word}")

    attempts = 3

    while attempts > 0:
        guess = input("Your guess: ").lower()

        if guess == original_word:
            print("Congratulations! You guessed the word correctly.")
            break
        else:
            print("Incorrect guess. Try again.")
            attempts -= 1

    if attempts == 0:
        print(f"Sorry, you've run out of attempts. The correct word was '{original_word}'.")

if __name__ == "__main__":
    word_scramble()
