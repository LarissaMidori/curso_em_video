''' Faça um programa que mostre na tela uma contagem regressiva para o Ano Novo, indo de 10 até 0, com uma pausa de 1 segundo entre eles. '''

from time import sleep
from emoji import emojize

for i in range(10, 0, -1):
    print(i)
    sleep(1)
print(f'{emojize(":fireworks:")}')
print(f'Feliz ANo Novo!!')
