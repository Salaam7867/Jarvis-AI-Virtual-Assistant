import os
import pyautogui
import screen_brightness_control as sbc
from ai_module import get_ai_command

def open_app(app_name):
    app_name = app_name.lower().strip()

    apps = {
        "chrome": "chrome",
        "edge": "msedge",
        "notepad": "notepad",
        "calculator": "calc",
        "cmd": "cmd",
        "powershell": "powershell",
        "outlook": "outlook",
        "word": "winword",
        "excel": "excel",
        "whatsapp": "whatsapp:",
    }

    for key in apps:
        if key in app_name:
            os.system(f"start {apps[key]}")
            return f"Opening {key}"

    # fallback
    os.system(f'start "" "{app_name}"')
    return f"Trying to open {app_name}"

def close_app(app_name):
    app_name = clean_target(app_name)

    mapping = {
        "chrome": "chrome.exe",
        "edge": "msedge.exe",
        "notepad": "notepad.exe",
        "outlook": "outlook.exe"
    }

    exe = mapping.get(app_name, f"{app_name}.exe")

    os.system(f"taskkill /f /im {exe}")
    return f"Closing {app_name}"

def clean_target(target):
    target = target.lower()

    if "chrome" in target:
        return "chrome"
    if "edge" in target:
        return "edge"
    if "notepad" in target:
        return "notepad"
    if "outlook" in target:
        return "outlook"
    if "whatsapp" in target:
        return "whatsapp"

    return target

def control_brightness(query):
    if "increase" in query:
        sbc.set_brightness(100)
        return "Brightness increased"
    elif "decrease" in query:
        sbc.set_brightness(30)
        return "Brightness decreased"
    return "Brightness adjusted"

def execute_task(query):
    action, target,response = get_ai_command(query)
    
    print("AI:", action, target)
    if action == "chat":
        return response

    if "open_app" in action:
        return open_app(target)

    elif "close_app" in action:
        return close_app(target)

    elif "volume" in action:
        pyautogui.press("volumeup")
        return "Volume adjusted"

    elif "brightness" in action:
        return control_brightness(query)

    elif "screenshot" in action:
        img = pyautogui.screenshot()
        img.save("screenshot.png")
        return "Screenshot taken"

    return "I didn't understand"