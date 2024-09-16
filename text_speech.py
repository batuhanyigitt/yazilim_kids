

import tkinter as tk
from gtts import gTTS
import os
import subprocess

def text_to_speech():
    text = text_entry.get()
    tts = gTTS(text=text, lang='tr')
    tts.save("output.mp3")


    subprocess.run(["start", "output.mp3"], shell=True)

    os.remove("output.mp3")

root = tk.Tk()
root.title("Text-to-Speech Player")

text_label = tk.Label(root, text="Enter the text:")
text_label.pack()

text_entry = tk.Entry(root, width=40)
text_entry.pack()

play_button = tk.Button(root, text="Play", command=text_to_speech)
play_button.pack()

root.mainloop()
