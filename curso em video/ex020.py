from random import shuffle
n1 = str(input('aluno 1: '))
n2 = str(input('aluno 2: '))
n3 = str(input('aluno 3: '))
n4 = str(input('aluno 4: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('a ordem e:')
print(lista)
