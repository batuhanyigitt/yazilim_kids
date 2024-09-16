import random
quiz_questions = [
    {
        "question": "What is the capital of France?",
        "options": ["London", "Berlin", "Paris", "Madrid"],
        "correct_answer": "Paris"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Mars", "Venus", "Jupiter", "Saturn"],
        "correct_answer": "Mars"
    },
]
def ask_question(question_data):
    print(question_data["question"])
    for i, option in enumerate(question_data["options"], 1):
        print(f"{i}. {option}")
    while True:
        try:
            user_choice = int(input("Enter the number of your answer: "))
            if 1 <= user_choice <= len(question_data["options"]):
                return question_data["options"][user_choice - 1]
            else:
                print("Invalid choice. Please choose a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number.")
def quiz_game():
    score = 0
    random.shuffle(quiz_questions)
    print("Welcome to the Quiz Game!\n")
    for question_data in quiz_questions:
        user_answer = ask_question(question_data)
        if user_answer == question_data["correct_answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {question_data['correct_answer']}\n")
    print(f"You scored {score} out of {len(quiz_questions)}.")
if __name__ == "__main__":
    quiz_game()
