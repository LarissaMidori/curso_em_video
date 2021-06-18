''' Desenvolva um programa que leia 6 valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares. '''

par = 0
valores = (int(input('Digite o 1º nº: ')), int(input('Digite o 2º nº: ')), int(input('Digite o 3º nº: ')), int(input('Digite o 4º nº: ')), int(input('Digite o 5º nº: ')), int(input('Digite o 6º nº: ')))
print(valores)
print(f'O valor 9 apareceu {valores.count(9)} vez(es).')
if 3 in valores:
    print(f'O primeiro valor 3 foi digitado na posição {valores.index(3) + 1}.')
else:
    print(f'O valor 3 não foi encontrado.')
print(f'Nºs pares digitados: ', end= '')
for i in valores:
    if i % 2 == 0:
        par += i
        print(f'{i} ', end= '')
