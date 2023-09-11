cont = 1
bolean = False
while not bolean == True:
    tab = int(input('qual taboada você quer ver? '))
    if tab < 0:
        break
    for a in range(10):
        tot = tab * cont
        print(f'{tab} X {cont} = {tot}')
        cont += 1
print('fim do programa, volte sempre!')
