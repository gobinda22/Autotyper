import pyautogui
import time
time.sleep(3)
text = """ copy here """
u = text.upper()
pyautogui.hotkey('capslock')
pyautogui.typewrite(u, interval = 0.05)


