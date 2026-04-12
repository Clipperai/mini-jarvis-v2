from voice import speak
from commands import run_command
from listener import take_command
from plyer import notification

notification.notify(
    title="1 Notification",
    message="Jarvis Activated",
    timeout=5
) # type: ignore


speak("Jarvis Activated")


while True:
    command = take_command()
    notification.notify(
    title="1 Notification",
    message=command,
    timeout=5
) # type: ignore
    if command == 'exit':
        
        notification.notify(
            title="1 Notification",
            message="Goodbye",
            timeout=5
            ) # type: ignore
        speak("Goodbye")
        break

    elif command == "":
        continue

    run_command(command)

    