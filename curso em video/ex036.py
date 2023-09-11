from termcolor import colored
from sys import exit
casa = float(input(colored('qual o valor da casa: R$', 'green')))
salario = float(input(colored('qual seu salario do comprador: ', 'blue')))
ano = int(input(colored('quantos anos de financiamento: ', 'magenta')))
if ano == 0:
    print('para de tentar bugar o sistema não vai dar certo. . .')
    exit()
elif ano >= 100:
    print('A PARTIR DE 100 ANOS O IMPRESTIMO E CANCELADO')
    exit()
prestasao =int( casa / (ano * 12) + 1 / 100)
salariomin = salario * 30 / 100
print(colored('para comprar uma casa de R${:.2f} em {} anos', 'yellow').format(casa, ano))
print(colored('a prestação sera de R${:.2f}', 'yellow').format(prestasao))
if prestasao <= salariomin:
    print(colored('O SEU IMPRESTIMO FOI ACEITO', 'blue'))
else:
    print(colored('O SEU IMPRESTIMO FOI NEGADO', 'red'))
