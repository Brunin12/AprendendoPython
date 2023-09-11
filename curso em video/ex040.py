n1 = float(input('qual e a nota do aluno(a): '))
n2 = float(input('qual e a segunda nota do aluno(a): '))
media = (n1 + n2) / 2
print('se as notas são {:.1f} e {:.1f} então a media do aluno(a) e de {:.1f}'.format(n1, n2, media))
if media < 5:
    print('           \033[1;31;47mREPROVADO\033[m')
elif 5 >= media <= 6.9:
    print('           \033[1;31;47mRECUPERAÇAO\033[m')
else:
    print('           \033[1;32;40mAPROVADO\033[m')
