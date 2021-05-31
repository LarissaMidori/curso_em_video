# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))
num3 = int(input('Terceiro número: '))
# Descobrindo quem é o menor
menor = num1
if num2 < num1 and num2 < num3 :
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3
# Descobrindo quem é o maior
maior = num1 
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3
print(f'O maior é o número {maior} e o menor é o número {menor}.')
