salario = float(input('qual e o salário do(a) Funcionário(a)? R$'))
al = int(input('qual o aumento dele(a) %'))
novo = salario + (salario * al / 100)
print('o funcionário que ganhava {} agora com {}% de aumento, passa a receber {}R$!'.format(salario, al, novo))
