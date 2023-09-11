viagem = float(input('qual a distania da sua viagem: '))
if viagem <= 200:
    preco = viagem * 0.50
else:
    preco = viagem * 0.45
print('o preço da sua viagem e R$ {:.2f}'.format(preco))
