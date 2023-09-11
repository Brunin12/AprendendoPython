from time import sleep
from sys import exit
n1 = int(input('digite um valor: '))
n2 = int(input('digite outro valor: '))
escolha = 0
while not escolha == 5:
    print('''====== VAR MENU ======
[ 1 ] SOMAR
[ 2 ] MULTIPLICAR
[ 3 ] MAIOR
[ 4 ] NOVOS NÚMEROS
[ 5 ] SAIR''')
    escolha = int(input('Qual sua escolha: '))
    if escolha == 1:
        s = n1 + n2
        print('a soma de {} e {} e {}'.format(n1, n2, s))
        sleep(1)
    elif escolha == 2:
        s = n1 * n2
        print(' {} x {} a multiplicação deu {}'.format(n1, n2, s))
        sleep(1)
    elif escolha == 3:
        if n1 > n2:
            print('o {} e maior que {}'.format(n1, n2))
        else:
            print('o {} e maior que {}'.format(n2, n1))
        sleep(1)
    elif escolha == 4:
        print('informe os numeros novamente')
        n1 = int(input('Digite um numero: '))
        n2 = int(input('Digite outro numero: '))
        sleep(1)
    elif escolha == 5:
        print('finalizando. . .')
        sleep(2)
        exit()
    else:
        print('====== INVALIDO TENTE NOVAMENTE ======')
        sleep(1)
