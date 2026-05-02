import os
import re
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def get_ai_command(query):
    try:
        prompt = f"""
You are an AI assistant.

Your job:
1. If the query is a COMMAND → return:
action: <action>
target: <target>

2. If the query is a GENERAL QUESTION → return:
action: chat
target: none
response: <short answer>

Rules:
- No explanation
- Strict format
- Only required lines

Examples:

Query: open chrome
action: open_app
target: chrome

Query: take screenshot
action: screenshot
target: none

Query: who is elon musk
action: chat
target: none
response: Elon Musk is a billionaire entrepreneur and CEO of Tesla and SpaceX.

Query: {query}
"""

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}]
        )

        text = response.choices[0].message.content.lower()

        # 🔥 NEW PARSER
        action_match = re.search(r'action:\s*(\w+)', text)
        target_match = re.search(r'target:\s*(\w+)', text)
        response_match = re.search(r'response:\s*(.+)', text)

        action = action_match.group(1) if action_match else "unknown"
        target = target_match.group(1) if target_match else ""
        reply = response_match.group(1).strip() if response_match else ""

        return action, target, reply

    except Exception as e:
        print("Groq Error:", e)
        return "unknown", "", ""