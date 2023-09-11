from random import randint

numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10),
           randint(1, 10), )
print(f'os valores sorteados foram {numeros}')
for n in numeros:
    print(f'{n} ->', end=' ')
print('fim')
print(f'o maior valor foi {max(numeros)}')
print(f'o menor valor foi {min(numeros)}')
