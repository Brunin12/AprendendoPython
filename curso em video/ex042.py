from termcolor import *
print(colored('-=', 'blue') * 20)
print(colored('Analizador de triangulos', 'yellow'))
print(colored('-=', 'blue') * 20)
r1 = float(input(colored('primeiro segmento: ', 'magenta')))
r2 = float(input(colored('segundo segmento: ', 'green')))
r3 = float(input(colored('terceiro segmento: ', 'red')))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(colored('      OS SEGUIMENTOS FORMAM UM TRIANGULO ', 'green'))
    if r1 == r2 == r3:
        print(colored('    EQUILATERO!', 'yellow'))
    if r1 != r2 != r3 != r1:
        print('    \033[1mESCALENO\033[m')
    elif r1 == r3 and r1 != r2:
        print('    \033[1;47mISÓSELES\033[m')
else:
    print('           \033[41mNÃO FORMA UM TRIANGULO\033[m')
