
import os
import platform

def adjust_volume(level):
    if platform.system() == "Darwin":
        os.system(f"osascript -e 'set volume output volume {level}'")
    else:
        print(f"[Volume] Adjust to {level}% (Not supported on this OS)")

def switch_tab():
    if platform.system() == "Darwin":
        os.system("osascript -e 'tell application "System Events" to key code 48 using control down'")
    else:
        print("[Tab Switch] Triggered (Not supported on this OS)")
