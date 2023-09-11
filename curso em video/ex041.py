idade = int(input('qual sua idade: '))
if idade <= 9:
    print('sua categoria de atleta e \033[1;42mMIRIM\033[m')
elif idade <= 14:
    print('sua categoria de atleta e \033[1;45mINFANTIL\033[m')
elif idade <= 19:
    print('sua categoria e \033[1;46mJUNIOR\033[m')
elif idade <= 25:
    print('PARABENS SUA CATEGORIA DE ATLETA E \033[1;41mSENIOR\033[m')
elif idade >=100:
    print('carreira encerrada')
else:
    print('sua categoria de atleta e \033[1;47mMASTER\033[m :)')
