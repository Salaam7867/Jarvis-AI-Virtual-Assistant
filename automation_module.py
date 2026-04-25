import os
import pyautogui
import screen_brightness_control as sbc
from ai_module import get_ai_command

def open_app(app_name):
    try:
        os.system(f"start {app_name}")
        return f"Opening {app_name}"
    except:
        return "App not found"

def close_app(app_name):
    try:
        os.system(f"taskkill /f /im {app_name}.exe")
        return f"Closing {app_name}"
    except:
        return "Unable to close app"

def control_brightness(query):
    if "increase" in query:
        sbc.set_brightness(100)
        return "Brightness increased"
    elif "decrease" in query:
        sbc.set_brightness(30)
        return "Brightness decreased"
    return "Brightness adjusted"

def execute_task(query):
    action, target = get_ai_command(query)

    print("AI:", action, target)

    if action == "open_app":
        return open_app(target)

    elif action == "close_app":
        return close_app(target)

    elif action == "volume":
        pyautogui.press("volumeup")
        return "Volume adjusted"

    elif action == "brightness":
        return control_brightness(query)

    elif action == "screenshot":
        img = pyautogui.screenshot()
        img.save("screenshot.png")
        return "Screenshot taken"

    return "I didn't understand"