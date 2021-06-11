''' Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.'''

print(f'==== Gerador de P.A. ====')
termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
contador = 1
while contador <= 10:
    print(f'{termo} => ', end = '')
    termo += razao
    contador += 1
print(f'FIM!!')
