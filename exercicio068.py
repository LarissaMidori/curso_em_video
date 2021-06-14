'''  Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. '''

from random import randint

print(f'{"~+" * 20}')
print(f'{"PAR OU ÍMPAR":^40}')
print(f'{"~+" * 20}')
vitoria = 0
while True:
    computador = randint(0, 10)
    jogador = int(input('Diga um nº: '))
    total = jogador + computador
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Par ou Ímpar: (P/I) ')).strip().upper()[0]
    print(f'O jogador jogou {jogador} e o computador jogou {computador}. Total: {total}. ' , end = '')

    if total % 2 == 0:
        print(f'DEU PAR!')
    else:
        print(f'DEU ÍMPAR!')

    if escolha == 'P':
        if total % 2 == 0:
            print(f'VOCÊ VENCEU!')
            vitoria += 1
        else:
            print(f'VOCÊ PERDEU')
            break
    elif escolha == 'I':
        if total % 2 == 1 :
            print(f'VOCÊ VENCEU!')
            vitoria += 1
        else:
            print(f'VOCÊ PERDEU!')
            break
    print(f'Vamos jogar de novo!')
print(f'GAME OVER! Você ganhou {vitoria} vez(es).')
