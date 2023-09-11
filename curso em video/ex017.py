import math
co = float(input('comprimento do cateto oposto: '))
ca = float(input('combrimnto do cateto adjisente: '))
hi = math.hypot(co, ca)
print('a hipotenusa vai medir {:.2f}'.format(hi))
