''' Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
– O primeiro valor é maior
– O segundo valor é maior
– Não existe valor maior, os dois são iguais '''

num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))
if num1 > num2:
    print(f'O primeiro valor {num1}, é maior que {num2}.')
elif num2 > num1:
    print(f'O segundo valor {num2}, é maior que {num1}.')
else:
    print(f'Não existe valor maior. Os dois são iguais.')
