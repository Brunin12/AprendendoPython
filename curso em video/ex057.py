sx = 0
n = 0
while not n == 1:
    sx = str(input('qual seu sexo [M/F]: ')).upper()
    if sx == 'M':
        n = 1
    elif sx == 'F':
        n = 1
    if sx != 'M' and sx != 'F':
        print('invalido digite novamente')
print('fim')

