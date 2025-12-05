import pyautogui
import webbrowser
import time

webbrowser.open("https://www.python.org/ftp/python/3.10.0/python-3.10.0-amd64.exe")
time.sleep(1)
pyautogui.press('enter')
time.sleep(0.5)
pyautogui.hotkey('win', 'r')
pyautogui.press('backspace')
pyautogui.typewrite("cmd")
pyautogui.press('enter')
time.sleep(0.5)
pyautogui.typewrite("pip install pyautogui schedule colorama termcolor pyttsx3 pyfiglet rich pygame twilio")
pyautogui.press('enter')