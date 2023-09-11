prox = False
cont = 0
lap = 0
maior = 0
menor = 0
while not prox == True:
    n1 = float(input('Digite um numero: '))
    cont += n1
    lap += 1
    if lap == 1:
        maior = menor = n1
    else:
        if n1 > maior:
            maior = n1
        if n1 < menor:
            menor = n1
    prox = str(input('quer continuar [ S / N ]: ')).upper().strip() [0]
    if prox == 'N':
        prox = True
    elif prox == 'S':
        prox = False
    else:
        print('invalido')
media = cont / lap
print(f'a media dos valores e {media}', end=', ')
print('o maior numero e {} e o menor e {}'.format(maior, menor), end=', ')