from random import randint

v = 0
print('='*31)
print('Vamos jogar Par ou Ímpar')
print('='*31)
perdeu = False
while True:
    jogador = int(input('digite um valor: '))
    computador = randint(0, 11)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar [P/I]: ')).upper().split()[0]
    print(f'você jogou {jogador} e o computador jogou {computador}. total de {total}')
    if tipo == 'P':
        if total % 2 == 0:
            print('Deu ÍMPAR, você ganhou')
            v += 1
        else:
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Deu PAR, Você ganhou')
            v += 1
        else:
            break
    print('vamos jogar novamente. . . ')
if v <= 1:
    print(f'PERDEU, você conseguio ganhar {v} vez')
elif v >= 10:
    print(f'PARABENS, VOCÊ GANHOU {v} VEZES, ESSE E O NOVO RECORDE!!')
else:
    print(f'PERDEU, você conseguio ganhar {v} vezes')

