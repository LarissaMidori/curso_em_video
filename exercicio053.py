''' Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:

APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA. '''

''' frase = str(input('Digite uma frase: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra) # junto tudo em uma string
inverso = ''
for letra in range(len(junto) - 1, -1, -1): # comprimento de junto -1 para ter o comprimento da frase digitada, última letra, iteração de trá pra frente
    inverso += junto[letra]
print(f'Você digitou a frase: {frase} e o inverso dela é {inverso}.')
if inverso == junto:
    print(f'Temos um PALÍNDROMO.')
else:
    print(f'NÃO temos um palíndromo.') '''


# Versão sem for

frase = str(input('Digite a frase: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
fatiado = junto[::-1]
print(f'Frase digitada: {junto}. Inverso da frase: {fatiado}.')
if junto == fatiado:
    print(f'Temos um PALÍNDROMO.')
else:
    print(f'NÃO temos um palíndromo.')