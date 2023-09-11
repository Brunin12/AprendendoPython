maior = 0
menor = 0
soma = 0
for p in range(1, 6):
    peso = float(input('qual o peso da {}ª pessoa: '.format(p)))
    soma += peso
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('o menor peso lido foi {} KG'.format(menor))
print('o maior pesso lido foi {} KG'.format(maior))
print('s soma de todos os pessos e {} KG'.format(soma))
