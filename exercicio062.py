''' Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos. '''

print(f'==== Super analisador de P.A. ====')
termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
mais = 10
total = 0
cont = 1
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo} => ', end = '')
        termo += razao
        cont += 1
    print(f'Pausa')
    mais = int(input(f'Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {total} termos.')

