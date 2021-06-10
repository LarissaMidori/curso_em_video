''' Faça um programa que leia um número qualquer e mostre o seu fatorial. 
Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120 '''

''' 
from math import factorial

n = int(input('Digite um nº para calcular seu fatorial: '))
fatorial = factorial(n)
print(f'O fatorial de {n} é: {fatorial}.') 
'''

n = int(input('Digite um nº para calcular seu fatorial: '))
fatorial = 1
print(f'Calculando {n}! = ', end = '')
while n > 0:
    print(f'{n}', end = '')
    if n > 1:
        print(f' x ', end = '')
    else:
        print(f' = {fatorial}')
    fatorial *= n
    n -= 1 

'''
n = int(input('Digite um nº para calcular seu fatorial: '))
fatorial = 1
print(f'Calculando fatorial de {n}! = ', end = '')
for n in range(n, 0, -1):
    print(f'{n}', end = '')
    if n > 1:
        print(f' x ', end = '')
    else:
        print(f' = {fatorial}')
    fatorial *= n '''

'''
n = int(input('Digite um nº para calcular seu fatorial: '))
fatorial = 1
c = n
for n in range(n, 0 , -1):
    fatorial *= n
print(f'O fatorial de {c}! é {fatorial}.')
'''
