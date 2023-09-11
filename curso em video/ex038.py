from termcolor import colored
n1 = float(input(colored('digite um numero: ', 'blue')))
n2 = float(input(colored('digite outro numero: ', 'red')))
if n1 > n2:
    print(colored('o primeiro numero digitado e o maior', 'yellow'))
elif n2 > n1:
    print(colored('o segundo numero e maior: ', 'magenta'))
elif n1 == n2:
    print(colored('não existe numero maior', 'green'))