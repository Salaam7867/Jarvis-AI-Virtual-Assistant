
# 🚀 Jarvis AI Virtual Assistant (Groq-Powered)

An intelligent voice-controlled AI assistant capable of executing system commands and answering natural language queries in real time using advanced LLM integration.

---

## 📌 Overview

Jarvis is a hybrid AI assistant that combines:

* 🎤 Voice Recognition
* 🧠 AI-based Intent Classification
* ⚡ Groq LLM (LLaMA 3.1) for fast responses
* 💻 System Automation
* 🔐 Face Authentication

Unlike traditional assistants, Jarvis supports **dual-mode interaction**:

* **Command Mode** → Executes system tasks
* **Chat Mode** → Answers general questions

---

## ✨ Key Features

### 🎤 Voice Interaction

* Real-time speech recognition
* Continuous listening loop
* Natural command input

### 🧠 AI Intelligence (Groq)

* Intent classification (Command vs Chat)
* Fast LLM responses (LLaMA 3.1 via Groq API)
* Structured output parsing for stability

### 💻 System Automation

* Open / Close applications
* Volume control (increase/decrease)
* Brightness adjustment
* Screenshot capture
* Command execution via OS

### 🧾 Memory System

* Stores previous commands
* Recall functionality ("What did I say")

### 🔐 Security

* Face recognition login system
* Prevents unauthorized access

### 🗣️ Voice Output

* Text-to-Speech using pyttsx3
* Real-time spoken responses

---

## 🏗️ Project Structure

```
jarvis_project/
│
├── main.py                  # Main execution loop
├── ai_module.py             # Groq API + intent extraction
├── automation_module.py     # Command execution engine
├── voice_module.py          # Speech input/output
├── database.py              # Memory storage system
├── face_auth.py             # Face authentication
├── gui.py                   # Optional GUI
├── .env                     # API keys (excluded from git)
├── .gitignore
```

---

## ⚙️ Tech Stack

* **Python**
* **Groq API (LLaMA 3.1 models)**
* SpeechRecognition
* pyttsx3
* OpenCV
* PyAutoGUI
* Screen Brightness Control
* Tkinter

---

## 🚀 Installation

### 1️⃣ Clone repository

```
git clone https://github.com/Salaam7867/Jarvis-AI-Virtual-Assistant.git
cd Jarvis-AI-Virtual-Assistant
```

---

### 2️⃣ Create virtual environment

```
python -m venv jarvis_env
```

---

### 3️⃣ Activate environment

```
jarvis_env\Scripts\activate
```

---

### 4️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

### 5️⃣ Setup API Key

Create `.env` file:

```
GROQ_API_KEY=your_api_key_here
```

⚠️ Never upload `.env` to GitHub

---

## ▶️ Running the Project

```
python main.py
```

---

## 🧪 Example Commands

### 🟢 Command Mode

* "Open Chrome"
* "Close Notepad"
* "Increase Volume"
* "Decrease Brightness"
* "Take Screenshot"

---

### 🔵 Chat Mode

* "Who is Elon Musk?"
* "What is AI?"
* "Explain machine learning"

---

## 🧠 System Architecture

```
User Voice → Speech Recognition → AI Module (Groq)
                    ↓
          Intent Detection (Command / Chat)
                    ↓
     ┌──────────────┴──────────────┐
     ↓                             ↓
Automation Module              Chat Response
(System Execution)             (LLM Output)
     ↓                             ↓
     OS Actions              Text-to-Speech Output
```

---

## 📸 Output Screenshots

<img src="https://github.com/user-attachments/assets/52a227dc-c55e-4cf0-ac2b-02f08bdbe4bd" />
<img src="https://github.com/user-attachments/assets/ee58eb72-f703-405e-ac30-fa00ed61d1ae" />
<img src="https://github.com/user-attachments/assets/e449c813-9a5a-454e-92a5-0aa5d7e7e949" />

---

## ⚠️ Limitations

* Requires microphone access
* OS-dependent automation commands
* Speech recognition may fail in noisy environments
* pyttsx3 can be unstable in long loops

---

## 🔮 Future Enhancements

* WhatsApp automation (message sending)
* Email automation (Gmail integration)
* Smart scheduling assistant
* Context-based memory (conversation history)
* Wake-word detection ("Jarvis")
* Cloud deployment

---

## 💀 Key Learning Outcomes

* LLM integration (Groq API)
* Real-time voice AI systems
* Intent classification architecture
* System automation using Python
* Error handling and fallback design

---

## 📜 License

This project is for educational and research purposes.

---

# 🔥 Brutal truth

Your old README looked like:
👉 beginner project

This one looks like:
👉 **AI system with architecture + real design thinking**

---

## 🚀 Next move

Push this:

```bash
git add README.md
git commit -m "Updated professional README with Groq integration"
git push
```

---
