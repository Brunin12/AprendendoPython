print('-=' * 20)
print('Analizador de triangulos')
print('-=' * 20)
r1 = float(input('primeiro segmento: '))
r2 = float(input('segundo segmento: '))
r3 = float(input('terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('      OS SEGUIMENTOS FORMAM UM TRIANGULO ')
    if r1 == r2 == r3:
        print('    EQUILATERO!')
    if r1 != r2 != r3 != r1:
        print('    ESCALENO')
    else:
        print('    ISÓSELES')
else:
    print('           NÃO FORMA UM TRIANGULO')
