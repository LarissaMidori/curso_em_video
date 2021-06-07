# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
total = 0
num = int(input('Digite um número: '))
for i in range(1, num + 1):
    if num % i == 0: # nºs primos são divididos por 1 e por ele mesmo
        total += 1
        print(f'O número {num} é divisível por {i}.')
if total == 2:
    print(f'O número {num} é PRIMO.')
else:
    print(f'O número {num} NÃO É PRIMO.')
    