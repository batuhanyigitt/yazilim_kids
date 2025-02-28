
import tkinter as tk 
from gtts import gTTS 
from pydub import AudioSegment
from pydub.playback import play 
import os 

def text_to_speech():
    text = text_entry.get()
    tts = gTTS(text=text, lang='en')  
    tts.save("output.mp3")
    
    audio = AudioSegment.from_mp3("output.mp3")
    play(audio)
    
    os.remove("output.mp3")
     
root = tk.Tk()
root.title("metin okuyucu")

text_label = tk.Label(root, text="Enter text(Yazmak istediginiz metni giriniz):")
text_label.pack()

text_entry = tk.Entry(root, width=50) 
text_entry.pack()

play_button = tk.Button(root, text="Play", command=text_to_speech)
play_button.pack()

root.mainloop()
