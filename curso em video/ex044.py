from sys import exit
print('=================LOJAS BR1=================')
compras = float(input('quanto você comprou na loja do br1: '))
print('''   \033[1;47mQUAL O MEIO DE PAGAMENTO?\033[m                 
\033[1;44m[ 1 ] A VISTA (dinheiro / cheque)\033[m
\033[1;46m[ 2 ] A VISTA (cartão)\033[m
\033[1;43m[ 3 ] 2X  NO  (sem juros)\033[m
\033[1;45m[ 4 ] 3X OU MAIS NO CARTÃO\033[m''')
escolha = int(input('     QUAL SUA ESCOLHA: '))
if escolha == 0 or escolha >= 5:
    print('\033[1;41mNUMERO INVALIDO\033[m')
elif escolha == 1:
    total = compras - (compras * 10 / 100)
    print('\033[1;47mO VALOR DAS COMPRA FOI DE {:.2F} NO DINHEIRO\033[m'.format(total))
elif escolha == 2:
    total = compras - (compras * 5/100)
    print('\033[1;47mO VALOR DAS COMPRA FOI DE {:.2F} NO CARTÃO\033[m'.format(total))
elif escolha == 3:
    total = compras
    parcelas = total / 2
    print('\033[1;47mSUA COMPRA SERA PARCELADA 2X DE {}'.format(parcelas))
    print('SUA COMPRA DE {:.2f} VAI CUSTAR R${:.2f} NO FINAL '.format(compras, total))
elif escolha == 4:
    total = compras + (compras * 20 / 100)
    totparc = int(input('\033[1;44mQUANTAS PARCELAS:\033[m '))
    if totparc < 3:
        print('\033[1;47mNA ESCOLHA 4 E IMPOCIVEL PARCELAR POR {}\033[m'.format(totparc))
        exit()
    parcelas = total / totparc
    print('\033[1;47mSUA COMPRA SERA PARCELADA {} VEZES DE R${:.2f}\033[m'.format(totparc, parcelas))
    print('\033[1;47mSUA COMPRA FOI PARCELADA POR {} E GANHOU 20% DE JUROS\033[m'.format(totparc))
    print('\033[1;44mO VALOR DA COMPRA E DE {} PASSA A SER DE {}\033[m'.format(compras, total))