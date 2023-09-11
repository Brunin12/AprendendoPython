salario = float(input('qual o salario do funcionario: '))
if salario <= 18250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('o salario do funcionario que era de R$ {}, agora e de {}'.format(salario, novo))
