from termcolor import colored

velocidade = float(input('a quantos km/h seu carro esta?: '))
multa = (velocidade - 80) * 7
if velocidade > 80:
    print(colored('-=-', 'yellow') * 29)
    print(colored('''você foi multado(a) por pasar do limite de velocidade que e de 80 km/h
    você'tera que pagar uma multa de R${:.2f} '''.format(multa), 'red'))
    print(colored('-=-', 'yellow') * 29)
print(colored('Tenha um bom dia! Dirija com cuidado!', 'yellow'))
