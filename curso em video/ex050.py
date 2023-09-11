cont = 0
soma = 0
for c in range(1, 7):
    num = int(input('digite o {} valor: '.format(c)))
    if num % 2 == 0 and num > 1:
        soma += num
        cont += 1
if cont == 1:
    print('voce informou 1 numero par, não tem mais nada para somar'.format(soma))
else:
    print('voce informou {} numeros pares a soma foi {}'.format(cont, soma))
input()
