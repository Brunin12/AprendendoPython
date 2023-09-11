idd18 = 0
homensCad = 0
mulheres20 = 0
while True:
    print('='*22)
    print('   CADASTRE UMA PESSOA')
    print('='*22)
    idade = int(input('Qual a idade da pessoa: '))
    if idade >= 18:
        idd18 += 1
    sexo = str(input('qual o sexo da pessoa [M/F]: ')).upper().split()[0]
    if sexo == 'F' and idade <= 20:
        mulheres20 += 1
    if sexo == 'M':
        homensCad += 1
    print('='*20)
    prox = str(input('quer continuar? [S/N]: ')).upper().split()[0]
    if prox == 'N':
        break
print('='*20)
print(f'''      NA SUA LISTA
TEM {idd18} PESSOAS COM MAIS DE 18 ANOS
TEM {homensCad} HOMENS CADASTRADOS
TEM {mulheres20} MULHERES COM MENOS DE 20 ANOS
''')
