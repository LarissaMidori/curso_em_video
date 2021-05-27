# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada

n = int(input('Digite um número para mostrar a tabuada: '))
print(f'{"-" * 30}')
print(f'A tabuada do número {n} é: ')
print(f'{"-" * 30}')
for i in range(11):
    print(f'{n} X {i} = {n*i}')
print(f'{"-" * 30}')