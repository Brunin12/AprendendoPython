from datetime import date
from sys import exit

atual = date.today().year
nacimento = int(input('em qual ano você nasceu: '))
if nacimento > atual:
    print('cyberpunk {}'.format(nacimento))
    exit()
idade = atual - nacimento
saldo = 18 - idade
print('quem naceu em {} tem {} anos em {}'.format(nacimento, idade, atual))
if idade == 18:
    print('Você pode se alistar')
elif idade < 18:
    ano = atual + saldo
    print('você tem {} anos ainda não tem idade para se alistar, faltam {} anos'.format(idade, saldo))
    print('seu alistamento vai ser em {}'.format(ano))
elif idade > 18:
    ano = atual - saldo
    print('você tem {} anos deveria ter se alistado a {} anos'.format(idade, saldo))

