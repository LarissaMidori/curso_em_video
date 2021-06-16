''' Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense. '''

times = ('FORTALEZA', 'ATHLETICO-PR', 'FLAMENGO', 'ATLÉTICO-GO', 'ATLÉTICO-MG', 'BRAGANTINO', 'FLUMINENSE', 'BAHIA', 'PALMEIRAS', 'CORINTHIANS', 'CEARÁ', 'SANTOS', 'INTERNACIONAL', 'JUVENTUDE', 'CUIABÁ', 'SPORT', 'SÃO PAULO', 'CHAPECOENSE', 'GRÊMIO', 'AMÉRICA-MG')
print(f'{"=~" * 26}')
print(f'Lista dos times do Brasileirão 2021: {times}.')
print(f'{"=~" * 26}')
print(f'Os 5 primeiros times são: {times[0:5]}.')
print(f'{"=~" * 26}')
print(f'Os últimos 4 colocados são: {times[-4:]}.')
print(f'{"=~" * 26}')
print(f'Os times em ordem alfabética são: {sorted(times)}.')
print(f'{"=~" * 26}')
print(f'O time da Chapecoense está na: {times.index("CHAPECOENSE")+1}ª posição.')
print(f'{"=~" * 26}')