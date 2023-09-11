print('===== GERADOR DE PA (2.0) =====')
num = int(input('digite um numero: '))
pul = int(input('pulando quantos numeros: '))
termo = num
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += pul
        cont += 1
    print('PAUSADO')
    mais = int(input('quanto você quer mosrar a mais? '))
print('Finalizando. . . O programa finalizado mostrou {} termos'.format(total))
