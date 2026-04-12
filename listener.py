import speech_recognition as sr

recognizer = sr.Recognizer()

def take_command():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio) #type: ignore
        command = command.lower()
        print("You said: " + command)
        return command
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        return ""