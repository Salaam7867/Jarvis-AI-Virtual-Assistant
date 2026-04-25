import requests

def get_ai_command(query):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": f"""
                Extract intent and target.

                Format:
                action: <action>
                target: <target>

                Actions:
                open_app
                close_app
                volume
                brightness
                screenshot
                unknown

                Query: {query}
                """,
                "stream": False
            }
        )

        text = response.json()['response'].lower()

        action = "unknown"
        target = ""

        for line in text.split("\n"):
            if "action" in line:
                action = line.split(":")[-1].strip()
            if "target" in line:
                target = line.split(":")[-1].strip()

        return action, target

    except Exception as e:
        print("AI Error:", e)
        return "unknown", ""