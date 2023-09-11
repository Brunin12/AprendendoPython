print('='*23)
print('Sequencia de Fibonacci')
print('='*23)
n = int(input('Quantos termos mostrar: '))
cont = 3
t1 = 0
t2 = 1
print('~'*30)
print('{} -> {}'.format(t1, t2), end='')
while cont <= n:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')

    t1 = t2
    t2 = t3
    cont += 1
print(' = FIM')
