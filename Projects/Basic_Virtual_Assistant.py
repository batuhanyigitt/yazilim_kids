import random
# Define a list of greetings and responses
greetings = ["hello", "hi", "hey", "greetings", "howdy"]
responses_to_greetings = ["Hello!", "Hi there!", "Hey!", "Greetings!", "Howdy!"]
# Define a list of questions and responses
questions = ["how are you", "what's up", "how's it going"]
responses_to_questions = ["I'm good, thanks!", "Not much, just chatting. How about you?"]
# Define a function to generate responses
def chatbot_response(input_text):
    input_text = input_text.lower()  # Convert input to lowercase
    # Check for greetings
    for greeting in greetings:
        if greeting in input_text:
            return random.choice(responses_to_greetings)
    # Check for questions
    for question in questions:
        if question in input_text:
            return random.choice(responses_to_questions)
    # If no match is found, respond with a default message
    return "I'm just a simple chatbot. I don't understand everything. Can you please rephrase that?"
# Main loop
print("Chatbot: Hello! How can I assist you today? (Type 'exit' to end)")
while True:
    user_input = input("User: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    response = chatbot_response(user_input)
    print("Chatbot:", response)