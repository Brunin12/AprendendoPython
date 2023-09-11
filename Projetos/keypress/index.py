from random import randint
from tkinter import *

import keyboard

palavras = ["jabuti", "Kaki", "janelas", "windows", "to com fome", "pc gamer", "anarquia", "tisunami", "mouse pad", "eletronica", "programação", "laboratorio"]

def Randword():
  return palavras[randint(0, 11)]

tela = Tk()
tela.geometry("400x400")
tela.configure(bg="gray")
tela.title("keypress + janelas")
tela.mainloop()
msg = "Nada ainda"
txt1 = Label(tela, text=msg)
txt1.grid(column=0, row=1)

while True:
  rand = Randword()
  inputo = keyboard.read_key()
  msg = f"Apertou a letra '{inputo}' de {rand}"
  txt1 = Label(tela, text=msg)
  txt1.grid(column=0, row=1)
  tela.mainloop()

