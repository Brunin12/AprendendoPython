F = 0
M = 0
maisvelho = 0
idadevelho = 0
menos20 = 0
homen = 0
mulher = 0
for p in range(1, 5):
    print('=========== {} PESSOA ============'.format(p))
    nome = str(input('qual seu nome: '))
    idade = int(input('qual a idade da {}ª pessoa: '.format(p)))
    sexo = str(input('qual su sexo [M/F]: ')).upper()
    if idade < 20 and sexo == 'F':
        menos20 += 1
        mulher += 1
    if sexo == 'M' and p == 1:
        maisvelho = nome
        idadevelho = idade
        homen += 1
    elif sexo == 'M':
        if idade > idadevelho:
            maisvelho = nome
if homen > 0:
    print('\033[1;47mo nome do homen mais velho e {}\033[m'.format(maisvelho))
elif homen == 0:
    print('\033[1;47mna sua lista não tem homens\033[m')
if mulher > 1:
    print('\033[1;47mexistem {} mulheres com menos de 20 anos na sua lista\033[m'.format(menos20))
elif mulher == 0:
    print('\033[1;47msua lista não tem mulheres\033[m')
elif mulher == 1:
    print('\033[1;47mexistem {} mulheres com menos de 20 anos na sua lista\033[m'.format(menos20))
