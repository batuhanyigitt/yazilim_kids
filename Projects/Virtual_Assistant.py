import random 
import webbrowser
import requests
from bs4 import BeautifulSoup
import spacy
import re
# load the spaCy for English model 
nlp = spacy.load('en_core_web_sm')
#Greeting function to user 
def greet():
    responses = ["Hello", "Hi there", "Hey! how can I help you?"]
    return random.choice(responses)
def respond(user_input):
    user_input = user_input.lower()
    
    if "hello" in user_input or "hi" in user_input:
        return greet()
    elif "how are you" in user_input or "how you feel today?" in user_input:
        return "I am fine, thank you. How can I help you?"
    elif "what is you name" in user_input:
        return "My name is Python Bot"
    elif "bye" in user_input or "goodbye" in user_input:
        return "Bye! take care.."
    
    elif "search" in user_input:
        query = user_input.replace("search", "").strip()
        search_url = f"https://www.google.com/search?q={query}"
        webbrowser.get(search_url)
        return f"here it's what you lookin for '{query}'."
    elif "weather" in user_input:
        doc = nlp(user_input)
        for entity in doc.ents:
            if entity.label == "GPE":
                location = entity.text
                weather_info = get_weather(location)
                return weather_info
            return "type again"
    else:
        return "Sorry! i couldnt' understand what you mean."
    
def get_weather(location):
    try:
        weather_url = f"https://weather.com/weather/today/l/{location}"
        response = requests.get(weather_url)
        soup = BeautifulSoup(response.content, "html.parser")
        temperature = soup.find("div", class_="today_nowcard-temp").text.strip()
        condition = soup.find("div", class_="today_nowcard-phares").text.strip()
    except:
        return "Sorry! I couldn't find the weather what you lookin for."

def main():
    print("welcome to Python Bot")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() ==  "quit":
            print("Python Bot: Bye! take care..")
            break
        response = respond(user_input)
        print("Python Bot:",  response)

if __name__ == "__main__":
    main()
    
    
    
    
    

    


    
    elif "search" in user_input:
        query = user_input.replace("search", "").strip()
        search_url = f"https://www.google.com/search?q={query}"
        webbrowser.open(search_url)
        return f"Here it's what you want '{query}'."
    elif "weather" in user_input:
        doc = nlp(user_input)
        for entity in doc.ents:
            if entity.label == "GPE":
                location = entity.text
                weather_info = get_weather(location)
                return weather_info
            return "Please type again"
    else:
        return "Sorry I don't understand you, write again."
         
def get_weather(location):
    try:
        weather_url = f"https://weather.com/weather/today/l/{location}"
        response = requests.get(weather_url)
        soup = BeautifulSoup(response.content, "html.parser")
        temperature = soup.find("div", class_="today_nowcard-temp").text.strip()
        condition = soup.find("div", class_="today_nowcard-phrase").text.strip()
        return f"The weather in {location} is {condition} with a temperature of {temperature}"
    except: 
        return "Sorry, I couldn't find the weather you mentioned."

def main():
    print("Hi, I'm Python Virtaul Assistant. How can I help you?")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Python Bot: Goodbye!") 
            break
        response = respond(user_input)
        print("Python Bot: ", response)

if __name__ == "__main__":
    main()   
    
    
    
    
    
    