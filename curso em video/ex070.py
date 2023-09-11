print('='*20)
print('  COMPRAS COM O SEU ZE')
print('='*20)
total = 0
cust1000 = 0
menor = 0
menorpreco = 0
precoBarato = 0
lap = 1
while True:
    nomeBarato = str(input('Qual o nome do produto: '))
    preco = float(input('Qual o preço do produto: R$'))
    if preco > 1000:
        cust1000 += 1
    total += preco
    if lap == 1:
        menor = nomeBarato
    elif lap > 1:
        if nomeBarato < menor:
            menor = nomeBarato
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
    elif continuar == 'S':
        lap += 1
print('='*20)
print(f''' NA SUA LISTA DE COMPRAS:
{total:.2f}$ EM COMPRAS
{cust1000} PRODUTO(S) QUE CUSTA(M) MAIS DE 1000$
{menor} FOI O PRODUTO MAIS BARATO''')
