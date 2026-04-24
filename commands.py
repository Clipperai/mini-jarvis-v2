from apps import open_app
import datetime
import webbrowser
from voice import speak



sites = {
    "google": "https://www.google.com",
    "youtube": "https://www.youtube.com",
    "gmail": "https://www.gmail.com"
}

def run_command(command):
    try: 
        if command.startswith("open"):
            command = command.replace('open', ' ').strip()
            if command in sites:
              webbrowser.open(sites[command])
              speak(f'Opening {command}')
            else:
              open_app(command)
        
        elif "time" in command:
            now = datetime.datetime.now()
            print("The Current time is " + now.strftime("%H:%M"))
            speak("The Current time is " + now.strftime("%H:%M"))
        
        elif "hello" in command:
            speak("Hello Sir, how can I assist you?")


        elif "search" in command:
            search_query = command.replace("search", "")
            webbrowser.open("https://www.google.com/search?q=" + search_query)
            speak("Searching for " + search_query)
    
    except:
        return ""
