cont = 0
lap = 0
while True:
    n = int(input('digite um numero [999 para parar]: '))
    if n == 999:
        break
    lap += 1
    cont += n
print(f'a soma dos {lap} valores deu {cont}')