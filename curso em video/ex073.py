times = ('corinthias', 'Palmeiras', 'Santos', 'Gremio', 'Cruzeiro','Flamengo', 'Vasco', 'Chapecoense', 'Atletico',
         'Botafogo', 'Atletico-PR', 'Bahia', 'São Paulo', 'Fluminense','Sport', 'Recife', 'EC Vitoria', 'Curitiba',
         'Avai', 'Ponte preta')
print('=-'*40)
print(f'Lista de times: {times}')
print('=-'*40)
print(f'os 5 primeiros são: {times[0:5]}')
print('=-'*40)
print(f'os 4 ultimos são {times[-4:]}')
print('=-'*40)
print(f'times em ordem alfabetica {sorted(times)}')
print('=-'*40)
print(f'o Chapecoense esta na {times.index("Chapecoense")+1}ª posição!')
