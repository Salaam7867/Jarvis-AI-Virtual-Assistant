import tkinter as tk
from tkinter import scrolledtext
from voice_module import take_command, speak
from automation_module import execute_task
from database import store_command, get_memory

def run_jarvis():
    query = take_command()

    if not query:
        return

    store_command(query)

    chat.insert(tk.END, "You: " + query + "\n")

    # 🔥 ONLY USE AI + AUTOMATION
    result = execute_task(query)

    if result:
        speak(result)
        chat.insert(tk.END, "Jarvis: " + result + "\n")
        return

    if "what did i say" in query:
        mem = get_memory()
        for m in mem:
            chat.insert(tk.END, "Memory: " + m + "\n")
        return

    speak("I did not understand")
    chat.insert(tk.END, "Jarvis: I did not understand\n")

# ✅ FIXED CONTINUOUS LOOP
def continuous_listen():
    run_jarvis()
    root.after(3000, continuous_listen)


# GUI Window
root = tk.Tk()
root.title("AI Virtual Assistant - Jarvis")
root.geometry("600x500")
root.configure(bg="#1e1e1e")

title = tk.Label(root, text="JARVIS AI ASSISTANT", font=("Arial", 16, "bold"), fg="white", bg="#1e1e1e")
title.pack(pady=10)

chat = scrolledtext.ScrolledText(root, width=70, height=20, bg="#2e2e2e", fg="white")
chat.pack(pady=10)

# ✅ Start listening automatically
root.after(1000, continuous_listen)

root.mainloop()