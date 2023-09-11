repetir = str(input('deseja que o programa se repita   (y/n): '))
if repetir == 'y':
    while True:
        a = str(input('primeiro numero: '))
        b = str(input('segundo numero: '))
        c = str(input('terceiro numero: '))
        empate = '1'
        menor = a
        if b < a and b < c:
            menor = b
        if c < a and c < b:
            menor = c
        maior = b
        if a > b and a > c:
            maior = a
        if c > b and c > a:
            maior = c
        if a == b and a == c:
            empate = '2'
            print('      EMPATE')
            print('''                             ''')
            print('''                             ''')
            print('''                             ''')
        if empate == '1':
            print('o maior valor digitado foi {}'.format(maior))
            print('o menor valor digitado foi {}'.format(menor))
            print('''                             ''')
            print('''                             ''')
            print('''                             ''')
else:
    a = str(input('primeiro numero: '))
    b = str(input('segundo numero: '))
    c = str(input('terceiro numero: '))
    empate = '1'
    menor = a
    if b < a and b < c:
        menor = b
    if c < a and c < b:
        menor = c
    maior = b
    if a > b and a > c:
        maior = a
    if c > b and c > a:
        maior = c
    if a == b and a == c:
        empate = '2'
        print('      EMPATE')
        print('        FIM        ')
    if empate == '1':
        print('o maior valor digitado foi {}'.format(maior))
        print('o menor valor digitado foi {}'.format(menor))
        print('  FIM')
        # /
         # /