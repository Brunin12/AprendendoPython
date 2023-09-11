import random

computador = random.randint(0, 10)

while True:
  usuario = int(input("digite um numero de [0 a 10]"))

  if usuario == computador:
    print("ganhoooou")
    break
  elif usuario < computador:
    print("mais")
  else:
    print("menos")
