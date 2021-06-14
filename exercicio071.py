''' Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS: considere que o caixa possui cédulas de R$100, R$50, R$20, R$10, R$5 e R$1. '''

valor = int(input('Qual o valor  ser sacado? R$ '))
if valor >= 100:
    cedula = valor // 100
    valor = valor % 100
    print(f'Total de {cedula} cédula(s) de R$ 100.')
if valor >= 50:
    cedula = valor // 50
    valor = valor % 50
    print(f'Total de {cedula} cédula(s) de R$ 50.')
if valor >= 20:
    cedula = valor // 20
    valor = valor % 20
    print(f'Total de {cedula} cédula(s) de R$ 20.')
if valor >= 10:
    cedula = valor // 10
    valor = valor % 10
    print(f'Total de {cedula} cédula(s) de R$ 10.')
if valor >= 5:
    cedula = valor // 5
    valor = valor % 5
    print(f'Total de {cedula} cédula(s) de R$ 5.')
if valor >= 1:
    cedula = valor // 1
    valor = valor % 1
    print(f'Total de {cedula} cédula(s) de R$ 1.')
