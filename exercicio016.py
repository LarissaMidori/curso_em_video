# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira

'''
from math import trunc # importando apenas um método
num = float(input('Digite um número real: '))
print(f'O número digitado é {num} e sua parte inteira é: {trunc(num)}')
'''
import math # importando todo módulo/biblioteca
num = float(input('Digite um número real: '))
print(f'O número é {num} e a parte inteira é {math.floor(num)}') # math.floor()
print(f'O número é {num} e a parte inteira é {math.trunc(num)}') # math.trunc()
print(f'O número é {num} e a parte inteira é {int(num)}') # int() 
