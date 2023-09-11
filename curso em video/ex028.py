from random import randint # IMPORTS
from termcolor import colored
import time # IMPORTS
while True:            # C/C+ JAVA XML
    IA = randint(0, 5)
    print(colored('-=-', 'yellow') * 19)
    # linhas
    print(colored('vou pensar em um numero de 0 a 5. tente adivinhar. . .', 'blue'))
    print(colored('-=-', 'yellow') * 19)
    # resposta do jogador
    jogador = int(input('em qual numero eu pensei?: '))
    print(colored('PROCESANDO. . .', 'magenta'))
    time.sleep(2)
    if jogador == IA:
        print(colored('PARABENS você me venceu, eu pensei no numero {}', 'green').format(IA))
    else:
        print(colored('GANHEI hahahah eu pensei em {} e não no {}', 'red').format(IA, jogador))

    time.sleep(3)
    print("""                                                                                 """)
while True:            # CODE IA LHC
    print('HHJ'.join('-'))
    # ENN CODE FILE FIND.rar
