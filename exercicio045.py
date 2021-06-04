# Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
from time import sleep

itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0,2)
print(f'{" JOKENPÔ! ":=^40}')
print(''' Escolha uma das opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA ''')
jogador = int(input('Escolha sua jogada: '))
if jogador > 2:
    print(f'JOGADA INVÁLIDA!! TENTE NOVAMENTE!')
else:
    print(f'JO...')
    sleep(1)
    print(f'KEN...')
    sleep(1)
    print(f'PÔ!!')
    if (computador == 0 and jogador == 0) or (computador == 1 and jogador == 1) or (computador == 2 and jogador == 2):
        resultado = 'EMPATE!'
    elif (computador == 0 and jogador == 2) or (computador == 1 and jogador == 0) or (computador == 2 and jogador == 1):
        resultado = 'O COMPUTADOR VENCE'
    elif (computador == 0 and jogador == 1) or (computador == 1 and jogador == 2) or (computador == 2 and jogador == 0):
        resultado = 'O JOGADOR VENCE'
    print(f'{"=#" * 15}')
    print(f'O jogador jogou {itens[jogador]}.')
    print(f'O computador jogou {itens[computador]}.') 
    print(f'{"=#" * 15}')
    print(f'{resultado}!!!')
