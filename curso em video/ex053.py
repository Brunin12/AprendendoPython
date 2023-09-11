frase = str(input('digite algo: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('{} reverso e {}'.format(junto, inverso))
if junto == inverso:
    print('a frase {} e um palíndromo'.format(junto))
else:
    print('a frase {} não e um palíndromo'.format(junto))
