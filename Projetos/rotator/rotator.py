import rotatescreen
from time import *


for i in range(0, 5) :
  screen = rotatescreen.get_primary_display()
  sleep(2)
  screen.set_landscape_flipped()
  sleep(2)
  screen.set_portrait_flipped()
  sleep(2)
  screen.set_landscape()
  sleep(2)
  screen.set_portrait()
  sleep(2)
  screen.set_portrait_flipped()
  sleep(2)
  screen.set_landscape()
  sleep(2)
