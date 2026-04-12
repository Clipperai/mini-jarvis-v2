from voice import speak
import pywhatkit as kit
import time
from voice import speak
from listener import take_command


# CONTACTS
contacts = {
    "home": "+919084877564",
    "vishu": "+919528185838"
}


def send_whatsapp_message():

    speak("Tell me the contact name")
    name = take_command()

    number = contacts.get(name)

    if number is None:
        speak("Contact not found")
        return


    speak("What message should I send")
    message = take_command()


    # speak("When should I send it?")
    # hour = int(input("Enter hour: "))
    # minute = int(input("Enter minute: "))

    speak("Tell me the hour")

    # hour_text = take_command()

    # if hour_text == "":
    #  speak("I did not hear the hour")
    #  return
 
    # hour = int(hour_text)


    # minute_text = take_command()

    # if minute_text == "":
    #     speak("I did not hear the minute")
    #     return

    # minute = int(minute_text)

    hour = int(input("Enter hour: "))
    speak("Tell me the minute")

    minute = int(input("Enter minute: "))

    speak("Tell me AM or PM: ")
    period = input("AM or PM: ").upper()

    # Convert to 24-hour format
    if period == "PM" and hour != 12:
        hour += 12

    elif period == "AM" and hour == 12:
        hour = 0


    try:
        kit.sendwhatmsg(
            number,
            message,
            hour,
            minute
        )

        time.sleep(5)
        speak("Message scheduled successfully")

    except Exception as e:
        print("Error:", e)
        speak("Failed to send message")