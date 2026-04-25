import pyttsx3
import speech_recognition as sr

# 🔊 Initialize engine ONCE
engine = pyttsx3.init()
engine.setProperty('rate', 150)

# ✅ FIXED SPEAK (NO THREADING)
def speak(text):
    print("Jarvis:", text)
    engine.stop()  # stop previous speech if any
    engine.say(text)
    engine.runAndWait()

# 🎤 TAKE COMMAND
def take_command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        try:
            print("Listening...")
            r.adjust_for_ambient_noise(source, duration=0.3)

            audio = r.listen(source, timeout=5, phrase_time_limit=5)

            query = r.recognize_google(audio)
            print("User:", query)
            return query.lower()

        except sr.WaitTimeoutError:
            return ""

        except sr.UnknownValueError:
            return ""

        except Exception as e:
            print("Mic error:", e)
            return ""