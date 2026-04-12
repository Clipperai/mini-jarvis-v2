import os
from voice import speak

def open_app(command):
    try:
        if os.system(f"start {command}") == 0:
            speak(f"Opening {command}")
        else:
            speak("app not found")
    except Exception as e:
        speak("oops! Application not found")
