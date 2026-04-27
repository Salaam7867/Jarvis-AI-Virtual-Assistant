# 🚀 Jarvis AI Virtual Assistant

A voice-controlled AI assistant powered by a local LLM (LLaMA3) for real-time system automation. The system runs locally, ensuring privacy, fast response, and no dependency on external APIs.

---

## 📌 Overview

Jarvis is an AI-based virtual assistant that processes natural language voice commands and performs system-level automation tasks such as opening applications, controlling system settings, and executing user-defined actions.

The system integrates:
- Speech Recognition
- Local AI Model (LLaMA3 via Ollama)
- Automation Module
- Memory Storage System

---

## ✨ Features

- 🎤 Voice Command Input
- 🧠 AI-Based Intent Recognition
- 💻 Open / Close Desktop Applications
- 🔊 Volume Control
- 💡 Brightness Control
- 📸 Screenshot Capture
- 🌐 Web Automation (Google / YouTube)
- 🧾 Memory Storage and Recall
- 🔐 Face Authentication Login

---

## 🏗️ Project Structure

jarvis_project/
│
├── main.py                  # Entry point
├── gui.py                   # GUI interface
├── ai_module.py             # AI processing (Ollama)
├── automation_module.py     # Task execution
├── voice_module.py          # Speech input/output
├── database.py              # Memory storage
├── face_auth.py             # Face authentication
├── jarvis_env/              # Virtual environment
└── .gitignore

---

## ⚙️ Tech Stack

- Python
- SpeechRecognition
- pyttsx3
- OpenCV
- PyAutoGUI
- Ollama (LLaMA3)
- Tkinter

---

## 🚀 Installation

1. Clone the repository:
   git clone https://github.com/Salaam7867/Jarvis-AI-Virtual-Assistant.git

2. Navigate to project:
   cd Jarvis-AI-Virtual-Assistant

3. Create virtual environment:
   python -m venv jarvis_env

4. Activate environment:
   jarvis_env\Scripts\activate

5. Install dependencies:
   pip install -r requirements.txt

---

## ▶️ Running the Project

Start Ollama (in a separate terminal):
   ollama run llama3

Run the assistant:
   python main.py

---

## 🧪 Example Commands

- "Open Chrome"
- "Open Calculator"
- "Increase Volume"
- "Take Screenshot"
- "What did I say"

---

## 📸 Output Screenshots

Include:
<img width="1920" height="1020" alt="Screenshot 2026-04-27 194833" src="https://github.com/user-attachments/assets/52a227dc-c55e-4cf0-ac2b-02f08bdbe4bd" />

<img width="1920" height="1080" alt="Screenshot 2026-04-27 195505" src="https://github.com/user-attachments/assets/ee58eb72-f703-405e-ac30-fa00ed61d1ae" />

<img width="1920" height="1080" alt="Screenshot 2026-04-27 195652" src="https://github.com/user-attachments/assets/e449c813-9a5a-454e-92a5-0aa5d7e7e949" />

---

## ⚠️ Limitations

- Requires microphone access
- Some system commands are OS-dependent
- Requires Ollama running locally

---

## 🔮 Future Improvements

- Email automation (Gmail integration)
- WhatsApp messaging automation
- Smart scheduling system
- More advanced NLP understanding

