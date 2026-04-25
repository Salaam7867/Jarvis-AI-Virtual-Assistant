from face_auth import face_login
from voice_module import speak, take_command
from automation_module import execute_task
from database import store_command, get_memory

def wish():
    speak("Initializing AI Virtual Assistant")
    speak("System ready")

if __name__ == "__main__":
    if face_login():
        wish()

    while True:
        query = take_command()

        if not query:
            continue  # skip empty input

        store_command(query)

        speak("Processing your request")

        # 🔥 AI + Automation (combined)
        result = execute_task(query)

        if result:
            speak(result)
            continue

        # 🧠 Memory Feature
        if "what did i say" in query:
            mem = get_memory()
            speak("You recently said")
            for m in mem:
                speak(m)
            continue

        # ❌ Exit
        if "exit" in query:
            speak("Shutting down")
            break

        speak("Sorry, I could not understand")