from datetime import date
totmaior = 0
totmenor = 0
atual = date.today().year
for pess in range(1, 8):
    nacs = int(input('em qual ano a {}ª pessoa nasceu: '.format(pess)))
    idade = atual - nacs
    if idade >= 18:
        totmaior += 1
    else:
        totmenor += 1
print('existem pessoas {} de menor e {} pessoas de maior na sua lista'.format(totmenor, totmaior))
