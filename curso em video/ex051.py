p1 = int(input('Primeiro numero: '))
p2 = int(input('Pulando: '))
decimo = p1 + (10 - 1) * p2
print('começando de {} ate 10 pulando {}'.format(p1, p2))
for c in range((p1), decimo + p2, (p2)):
    print('{}'.format(c),end='  ->  ')
print('Fim')