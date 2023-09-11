n = 0
cont = 0
while n != 999:
    n = int(input('digite um numero [ 999 para parar ]: '))
    if n == 999:
        break
    cont += n
# print('a soma deu {}'.format(cont))
print(f'a soma vale {cont: }')
