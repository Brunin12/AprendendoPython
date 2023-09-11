from termcolor import colored
repetir = str(input('deseja que o programa se repita? (y/n): '))
if repetir == 'y':
    while True:  # repetir
        numero = int(input(colored('digite um numero: ', 'magenta')))
        resultado = numero % 2
        if resultado == 1:
            print(colored('-=-', 'yellow') * 29)
            print(colored('o numero {} e impar', 'red').format(numero))
            print(colored('-=-', 'yellow') * 29)
            print('''                             ''')
            print('''                             ''')
            print('''                             ''')
        else:
            print(colored('-=-', 'yellow') * 29)
            print(colored('o numero {} e par', 'blue').format(numero))
            print(colored('-=-', 'yellow') * 29)
            print('''                             ''')
            print('''                             ''')
            print('''                             ''')  # repetir
else:  # sem repetir
    numero = int(input(colored('digite um numero: ', 'magenta')))
    resultado = numero % 2
    if resultado == 1:
        print(colored('-=-', 'yellow') * 29)
        print(colored('o numero {} e impar', 'red').format(numero))
        print(colored('-=-', 'yellow') * 29)
        print('''                             ''')
        print('''                             ''')
        print('''                             ''')
    else:
        print(colored('-=-', 'yellow') * 29)
        print(colored('o numero {} e par', 'blue').format(numero))
        print(colored('-=-', 'yellow') * 29)
        print('''                             ''')
        print('''                             ''')
        print('''                             ''')
