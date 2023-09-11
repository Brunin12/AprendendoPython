from time import sleep
from selenium.webdriver.common.keys import Keys
from tkinter import *

import pyautogui as pig

pig.PAUSE = 1

def exec_virus():
  pig.press("win")
  pig.write("cmd")
  pig.press("enter")
  sleep(3)
  pig.write(' python -u "c:\\Users\\Notebook\\Documents\\estudos\\python\\intencivao python\\aula3\\em_python.py"')
  pig.press("enter")




# INICIO
janela = Tk()

janela.title("o titulo aqui :)")

txt1 = Label(janela, text="execultar um codigo muito legal")
txt1.grid(column=0, row=0, padx=10, pady=10)

botao = Button(janela, text="iniciar", command=exec_virus)
botao.grid(column=0, row=1, padx=10, pady=10)




janela.mainloop()
# FIM