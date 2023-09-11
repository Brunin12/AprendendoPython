from sys import exit
from time import sleep
from random import randint
itens = ('pedra', 'papel', 'tesoura')
print('''Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] tesoura''')
jogador = int(input('Qual sua jogada: '))
if jogador >2:
    print('INVALIDO')
    exit()
computador = randint(0, 2)
print('PEDRA')
sleep(1)
print('PAPEL')
sleep(1)
print('TESOURA!!!')
print('-=' * 11)
print('computador jogou {}'.format(itens[computador]))
print('jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)
if computador == 0:   #jogou pedra
    if jogador == 0:
        print('empate')
    elif jogador == 1:
        print('jogador ganhou')
    elif jogador == 2:
        print('computador ganhou')
    else:
        print('invalido')
elif computador == 1:    #jogou papel
    if jogador == 0:
        print('computador ganhou')
    elif jogador == 1:
        print('empate')
    elif jogador == 2:
        print('jogador ganhou')
    else:
        print('invalido')
elif computador == 2:      #jogou tesoura
    if jogador == 0:
        print('jogador ganhou')
    elif jogador == 1:
        print('computador ganhou')
    elif jogador == 2:
        print('empate')
    else:
        print('invalido')