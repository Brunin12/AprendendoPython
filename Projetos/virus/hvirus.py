import time
import pyautogui



def get_ps(TEMPO=5):
    time.sleep(TEMPO)
    print(pyautogui.position())
    exit()

#get_ps()


pyautogui.PAUSE = 3

print("""









)
""")
gmail = str(input("qual seu gmail? \n"))
nome = str(input("qual seu nome? \n"))
m = int(input("mandar feadback no fim do programa? (1/0)\n"))


pyautogui.press("win")
pyautogui.write("Chrome")
time.sleep(5)
pyautogui.press("enter")
time.sleep(15)
pyautogui.write("dolar hoje")
pyautogui.press("enter")
time.sleep(10)
pyautogui.click(x=75, y=306, clicks=2)
pyautogui.hotkey("ctrl", "c")
pyautogui.hotkey("ctrl", "t")

time.sleep(2)
pyautogui.write("https://mail.google.com/mail/u/0/")
pyautogui.press("enter")
time.sleep(25)
pyautogui.click(x=29, y=169)
time.sleep(20)
pyautogui.write(gmail)
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.write(f"email sobre dolar hoje para o sr(a) {nome}")
pyautogui.press("tab")


pyautogui.write('Valor atual: RS')
pyautogui.hotkey("ctrl", "v")

pyautogui.hotkey("ctrl", "enter")
time.sleep(10)
if m == 1:
    pyautogui.press("win")
    pyautogui.write("discord")
    pyautogui.press("enter")

    time.sleep(5)
    pyautogui.click(x=40, y=47)
    pyautogui.click(x=156, y=218)

    pyautogui.write("manda robux pro @Java_lee pfv ele é lindo :(")
    pyautogui.press("enter")

