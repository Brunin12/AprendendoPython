from random import randint
tentativas = 0
r = randint(1, 10)
print('\033[1m='*30)
print('eu escolhi um numero entre 0 e 10 tente achar ele')
print('='*30)
while True:
    escolha = 0
    escolha = int(input('qual sua escolha: '))
    tentativas += 1
    if escolha == r:
        print('=' * 30)
        print('')
        print(f'\033[1;42mvocê ganhou em {tentativas} tentativas\033[m')
        print('\033[1m')
        print('=' * 30)
        break
    elif escolha > r:
        print('=' * 30)
        print('')
        print('menos. . . ',)
        print('')
        print('=' * 30)
    elif escolha < r:
        print('=' * 30)
        print('')
        print('mais. . . ')
        print('')
        print('=' * 30)
