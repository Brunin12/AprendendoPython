num = (int(input('digite um numero: ')),
       int(input('digite outro numero: ')),
       int(input('digite mais um numero: ')),
       int(input('digite o ultimo numero: ')))
print(f'você digitou os valores {num}')
print(f'o numero 9 apareceu {num.count(9)} vezes')
if 3 in num:
       print(f'o prmeiro 3 foi digitado na posição {num.index(3)+1}')
for n in num:
       if n % 2 == 0:
              print(f'na lista o(s) numero(s) par e {n} ', end=' ')
