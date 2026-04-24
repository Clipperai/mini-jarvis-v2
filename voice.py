import pyttsx3
    

def speak(text):
    try:
        engine = pyttsx3.init()
        engine.setProperty("rate", 190)

        print("Jarvis said:", text)
        engine.say(text)
        engine.runAndWait()
    except Exception as exc:
        print(f"Text-to-speech error: {exc}")
