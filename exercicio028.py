''' Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu. '''

from random import randint
from time import sleep

computador = randint(0,5) # faz gerar um valor entre 0 e 5
print(f'{"=+=" * 20}')
print(f'Vou pensar em um número entre 0 e 5! Tente advinhar!!')
print(f'{"=+=" * 20}')
jogador = int(input('Em que número eu pensei? ')) # a pessoa digita um número tentando advinhar
print(f'PROCESSANDO...')
sleep(1)
print(f'Pensei no número {computador}')
if(jogador == computador):
    print('Parabéns, você acertou!')
else:
    print(f'Você errou! Eu pensei no número {computador} e você no número {jogador}!')
