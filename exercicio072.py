''' Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso. '''

num = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    lerNum = int(input('Digite um nº entre 0 e 20: '))
    if lerNum <= 20 and lerNum >= 0:
        print(f'Você digitou o nº {num[lerNum]}.')
    else:
        print(f'Valor inválido! Tente novamente.') 
    continua = ' '
    while continua not in 'SN':
        print('=' * 25)
        continua = str(input('Deseja continuar? (S/N) ')).strip().upper()[0]
    if continua == 'N':
        break
print(f'Programa finalizado! Tenha um bom dia!')
