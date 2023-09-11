print('====== Gerador de PA ======')
num = int(input('digite um numero: '))
pul = int(input('pulando quantos numeros: '))
termo = num
cont = 1
while cont <= 10:
    print('{} -> '.format(cont), end='')
    termo += pul
    cont += 1
print('Fim')
