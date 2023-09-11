from time import sleep
num = int(input('digite um numero para ver sua tabuada: '))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(num, c, num*c))
    sleep(0.5)
