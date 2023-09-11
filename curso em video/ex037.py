from termcolor import colored
numero = int(input(colored('digite um numero inteiro: ', 'blue')))
print('''\033[1;47mescolha uma das bases para coversão:\033[m
\033[1;42m[ 1 ] BINARIO\033[m
\033[1;43m[ 2 ] OCTAL\033[m
\033[1;46m[ 3 ] HEXADECIMAL\033[m''')
ops = int(input('\033[1;47mqual sua decição:\033[m '))
if ops > 3:
    print('INVALIDO')
if ops == 1:
    print('\033[1;42m{} \033[m\033[1;42mconvertido em BINARIO e: {}\033[m'.format(numero, bin(numero)[2:]))
elif ops == 2:
    print('\033[1;43m{} \033[m\033[1;43mconvertido em OCTAL e: {}\033[m'.format(numero, oct(numero)[2:]))
elif ops == 3:
    print('\033[1;46m{} \033[m\033[1;46mconvertido em HEXADECIMAL e: {}\033[m'.format(numero, hex(numero)[2:]))
