import pyautogui
import pyperclip
import time
import pandas as pd

pyautogui.PAUSE = 1

# abrir navegador e enviar um link
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(5)
pyperclip.copy("https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?usp=sharing")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
time.sleep(20)

# entrar no arquivo exportar
pyautogui.click(339, y=269, clicks=2)
time.sleep(4)
pyautogui.click(339, y=269)

# baixar
time.sleep(3)
pyautogui.click(x=817, y=150)
time.sleep(3)
pyautogui.click(x=697, y=610)

# abrir gmail
time.sleep(3)
pyautogui.click(x=750, y=52, clicks=2)
pyautogui.hotkey("ctrl", "a")
pyperclip.copy("https://mail.google.com/mail/u/0/#inbox")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
time.sleep(10)
# ler os arquivos
dados = pd.read_excel(r"C:\Users\Notebook\Downloads\Vendas - Dez.xlsx")
faturamento = dados["Valor Final"].sum()
quant = dados["Quantidade"].sum()
print(faturamento, quant)
# enviar o gmail
pyautogui.click(x=64, y=165)
time.sleep(17)
pyautogui.write("brunoparreira77@gmail.com")
pyautogui.press("tab")
pyautogui.press("tab")

pyautogui.write("dados das lojas")
pyautogui.press("tab")
texto = f"""
Prezados, bom dia

O faturamento de ontem foi de R${faturamento:,.2f}
e vendemos {quant} unidades no total
"""
pyperclip.copy(texto)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("ctrl", "enter")
time.sleep(17)
pyautogui.hotkey("alt", "f4")
