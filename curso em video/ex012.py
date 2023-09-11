preço = float(input('qual o preço do produto? R$'))
desc = preço*95/100
print('o produto que custava {:.2f}R$, agora com 5% de desconto custa {:.2f}R$!'.format(preço, desc))
