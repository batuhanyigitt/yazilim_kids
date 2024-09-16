import pyttsx3

def get_available_voices():
    """
    Get available voices for text-to-speech conversion.

    Returns:
        list: Available voices.
    """
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    return voices

def set_voice(engine, voice_id):
    """
    Set the voice for text-to-speech conversion.

    Args:
        engine (pyttsx3.Engine): The pyttsx3 engine instance.
        voice_id (int): Index of the voice to set.
    """
    engine.setProperty('voice', voices[voice_id].id)

def text_to_speech(text, output_file="output.wav", rate=150, voice_id=0):
    """
    Convert text to speech using pyttsx3.

    Args:
        text (str): The text to convert to speech.
        output_file (str): File path to save the audio (default is "output.wav").
        rate (int): Speaking rate in words per minute (default is 150).
        voice_id (int): Index of the voice to use (default is 0).

    Returns:
        str: File path of the generated audio file.
    """
    engine = pyttsx3.init()
    engine.setProperty('rate', rate)
    set_voice(engine, voice_id)
    engine.save_to_file(text, output_file)
    engine.runAndWait()
    return output_file

if __name__ == "__main__":
    voices = get_available_voices()
    print("Available voices:")
    for i, voice in enumerate(voices):
        print(f"{i}. {voice.name}")

    voice_id = int(input("Select a voice by entering its index: "))
    input_text = input("Enter the text you want to convert to speech: ")
    output_file = text_to_speech(input_text, voice_id=voice_id)
    print(f"Text converted to speech. Audio file saved as: {output_file}")
