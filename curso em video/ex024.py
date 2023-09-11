cidade = str(input('qual o nome da sua cidade?: '))
cs = cidade.split()
s = 'silva' in cs[0]
print('sua cidade tem silva?: {}'.format(s))
