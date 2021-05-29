''' Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa. '''

from math import hypot

co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))
hip1 = hypot(co, ca)
hip2 = (co ** 2 + ca ** 2) ** (1/2)
print(f'O cateto oposto mede {co}, o cateto adjacente mede {ca} e a hipotenusa mede {hip1:.2f}.')
print(f'O cateto oposto vale {co}, o cateto adjacente vale {ca} e a hipotenusa vale {hip2:.2f}.')
