from random import randint
palpite = 0
computador = randint(0, 10)
print('oi eu sou seu pc e eu... acabei de pensar tente acertar de 1 a 10')
print('Sera que você consegue?')
acertou = False
while not acertou:
    jogador = int(input('Qual e seu palpite: '))
    palpite += 1
    if jogador > 10:
        print('invalido')
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('mais. . . tente novamente')
        elif jogador > computador:
            print('menos. . . tente novamente')
print('Acertou em {} tentativas'.format(palpite))





