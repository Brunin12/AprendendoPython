larg = float(input('largura da parede: '))
alt = float(input('altura da parede: '))
area = alt * larg
print('sua parede tem a dimenção de {}x{} e sua área é de {}m²'.format(larg, alt, area))
tinta = area / 2
print('para pintar essa área você precisará de {}L de tinta!'.format(tinta))