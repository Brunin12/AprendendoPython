kg = float(input('qual seu peso [KG] '))
altura = float(input('qual sua altura (M) '))
imc = kg / (altura ** 2)
print('o IMC do analizado e de {:.2f}'.format(imc))
if imc < 18.5 and imc > 1:
    print('A BAIXO DO PESSO')
elif imc <= 1:
    print('FORMIGA')
elif imc >= 100:
    print('BALÃO DE AR QUENTE')
elif imc >= 18.5 and imc < 25:
    print('PESO IDEAL')
elif imc >= 25 and imc < 30:
    print('SOBRE PESO')
elif imc >= 30 and imc <= 40:
    print('OBESIDADE')
elif imc > 40:
    print('OBESIDADE MORBIDA, cuidado')
