import pyautogui
import time
text = """ copy here """
u = text.upper()
pyautogui.hotkey('capslock')
pyautogui.typewrite(u, interval = 0.05)


