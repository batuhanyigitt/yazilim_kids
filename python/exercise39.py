import random

def choose_movie():
    movies = ["avatar", "inception", "jurassic park", "forrest gump", "gladiator", "titanic", "star wars"]
    return random.choice(movies)
def play_guess_the_movie():
    print("Welcome to Guess the Movie!")
    print("I will select a random movie title, and you have to guess the letters one at a time.")
    while True:
        movie = choose_movie()
        movie = movie.replace(" ", "")  
        movie_length = len(movie)
        guessed_movie = ["_"] * movie_length
        incorrect_attempts = 6  
        print(f"Movie title: {' '.join(guessed_movie)} (Length: {movie_length})")
        while incorrect_attempts > 0 and "_" in guessed_movie:
            guess = input(f"Guess a letter (Incorrect attempts left: {incorrect_attempts}): ").lower()
            if len(guess) != 1 or not guess.isalpha():
                print("Please enter a single letter.")
                continue
            if guess in movie:
                for i, letter in enumerate(movie):
                    if letter == guess:
                        guessed_movie[i] = guess
                print(f"Movie title: {' '.join(guessed_movie)} (Length: {movie_length})")
            else:
                print("Incorrect guess. Try again.")
                incorrect_attempts -= 1
        if "_" not in guessed_movie:
            print(f"Congratulations! You guessed the movie: {movie.replace(' ', ' ')}")
        else:
            print(f"Out of attempts. The movie title was: {movie.replace(' ', ' ')}")
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break
if __name__ == "__main__":
    play_guess_the_movie()
