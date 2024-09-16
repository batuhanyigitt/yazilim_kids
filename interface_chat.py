import tkinter as tk
from tkinter import scrolledtext
import random
class SimpleChatbot:
    def __init__(self, master):
        self.master = master
        master.title("Simple Chatbot")

        self.chatbox = scrolledtext.ScrolledText(master, wrap=tk.WORD, width=40, height=10)
        self.chatbox.pack(padx=10, pady=10)

        self.entry_label = tk.Label(master, text="You:")
        self.entry_label.pack(pady=5)
        self.user_entry = tk.Entry(master, width=30)
        self.user_entry.pack(pady=10)

        self.chat_button = tk.Button(master, text="Send", command=self.send_message)
        self.chat_button.pack()

        self.bot_response_label = tk.Label(master, text="Chatbot:")
        self.bot_response_label.pack(pady=5)
        self.bot_response = scrolledtext.ScrolledText(master, wrap=tk.WORD, width=40, height=4, state=tk.DISABLED)
        self.bot_response.pack(padx=10, pady=5)

    def greet(self):
        greetings = ["Hello!", "Hi there!", "Hey!", "Greetings!"]
        return random.choice(greetings)

    def respond_to_question(self, question):
        if "how are you" in question:
            return "I'm just a computer program, but thanks for asking!"
        elif "your name" in question:
            return "benim adim mahmut"
        elif "bugun hava nasil" in question:
            return "ne bileyim ben"
        else:
            return "You can call me ChatGPT."
        
        
    def send_message(self):
        user_input = self.user_entry.get().lower()
        self.user_entry.delete(0, tk.END)
        
        if user_input == "bye":
            self.bot_response.config(state=tk.NORMAL)
            self.bot_response.insert(tk.END, "Goodbye!")
            self.bot_response.config(state=tk.DISABLED)
        else:
            response = self.respond_to_question(user_input)
            
            self.bot_response.config(state=tk.NORMAL)
            self.bot_response.insert(tk.END, f"{response}\n")
            self.bot_response.config(state=tk.DISABLED)
    
if __name__ == "__main__":
    root = tk.Tk()
    chatbot_app = SimpleChatbot(root)
    root.mainloop()