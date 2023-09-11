import math

an = float(input('digite o ângulo que você deseja: '))
seno = math.sin(math.radians(an))
print('o ângulo de {} tem o SENO de {:.2f}'.format(an, seno))
coseno = math.cos(math.radians(an))
print('o ângulo de {} tem o COSENO de {:.2f}'.format(an, coseno))
tangente = math.tan(math.radians(an))
print('o ângulo de {} tema TANGENTE de {:.2f}'.format(an,tangente))
