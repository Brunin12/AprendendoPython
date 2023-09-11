import turtle as tl
from time import *
import random

tl.Screen().title("Mechendo com turtle")
tl.Screen().bgcolor("red")
pen = tl.Turtle()
pen.color("black")
intervalo = 1



colors = ["black", "green", "white", "purple", "cyan"]

def ramo():
  pen.color(random.choise(colors))
  for i in range(3):
    for i in range(3):
        pen.forward(30)
        pen.backward(30)
        pen.right(45)
  pen.left(90)
  pen.backward(30)
  pen.left(45)
  pen.right(90)
  pen.forward(90)



def square():
  tl.Screen().bgcolor("cyan")
  pen.color("green")
  for i in range(4):
    pen.forward(100)
    pen.right(90)


tl.Screen().title("Modo lerdo 🐌")
# modo lerdo
pen.forward(100)
pen.right(90)
pen.forward(100)
pen.right(90)
pen.forward(100)
pen.right(90)
pen.forward(100)
pen.right(90)

sleep(intervalo)
pen.clear()
tl.Screen().bgcolor("purple")
pen.color("cyan")

tl.Screen().title("Modo meh 😎")
#modo meh
for i in range(4):
  pen.forward(100)
  pen.right(90)

sleep(intervalo)
pen.clear()
tl.Screen().title("Modo senior 🐱‍👤")
#modo senior
square()

tl.Screen().bgcolor("red")
pen.color("black")
for i in range(2):
  pen.forward(100)
  pen.right(60)
  pen.forward(100)
  pen.right(120)
