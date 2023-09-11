resp = 0
cont = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco',   # prefiria estar dormindo
        'seis', 'sete', 'oito', 'nove', 'dez',
        'onze', 'doze', 'treze', 'quatorze', 'quinze',
        'deseseis', 'deseste', 'desoito', 'dezenove', 'vinte')
while not resp == 'N': # ja pode dormir?
    while True:
        num: int = 0
        num = int(input('digite um numero de 0 a 20: '))
        if 0 <= num <= 20:
            break  # ja pode dormir?
        print('tente novamente. . . ', end='')
    print(f'você digitou o numero {cont[num]}')
    resp = str(input('Quer continuar [S/N]: ')).upper().split()[0]
    if resp not in 'NS':
        print('TENTE NOVAMENTE. . . ', end='')  # DURMIRRR
