''' Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer. '''

from random import randint
'''
tentativas = 0
jogador = 0
print(f'==== Advinhe o nº entre 0 e 10 ====')
computador = randint(0, 10)
while jogador != computador:
    jogador = int(input(f'Em que nº pensei? '))
    tentativas += 1
    if jogador == computador:
        print(f'Você acertou! Parabéns!')
    else:
        if jogador > computador:
            print(f'O nº em que pensei é menor. Tente mais uma vez.')
        else:
            print(f'O nº em que pensei é maior. Tente mais uma vez.')
print(f'Foram necessárias {tentativas} tentativas.') 

'''

tentativas = 0
acertou = False
print(f'=== Estou pensando em um nº entre 0 e 10. Tente advinhar! ===')
computador = randint(0, 10)
while not acertou:
    jogador = int(input('Em que nº pensei? '))
    tentativas += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador > computador:
            print(f'O nº é menor, tente novamente!')
        elif jogador < computador:
            print(f'O nº é maior, tente novamente!')
print(f'Você acertou com {tentativas} tentativa(s)! Parabéns!!')
