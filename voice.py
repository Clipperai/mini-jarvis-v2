import pyttsx3

def speak(text):
   try:
    engine = pyttsx3.init()
    engine.setProperty('rate', 180)

    print("Jarvis said: ",text)
    engine.say(text)
    engine.runAndWait()

   except:
     print("Error")
       

