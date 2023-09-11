import time
import pyautogui
import pyperclip


pyautogui.PAUSE = 1

pyautogui.hotkey("win", "r")
pyautogui.write("cmd")
pyautogui.press("enter")
pyperclip.copy('python -u "c:\\Users\\Notebook\\Documents\\estudos\\python\\Projetos\\hvirus.py"')
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
