n = int(input('digite um numero para caucular seu fatorial: '))
c = n
f = 1
while c > 1:
    print('{}'.format(c), end='')
    print(' x 'if c > 2 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))