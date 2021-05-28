''' Faça um programa que leia a largura e a altura de uma parede, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada 1 litro de tinta, pinta uma área de 2m² '''

altura = float(input('Qual é a altura da parede em metros? '))
largura = float(input('Qual é a largura da parede em metros? '))
area = altura * largura
print(f'A parede tem {altura:.2f}m de altura e {largura:.2f}m de largura e uma área de {area:.2f}m². \n Precisaremos de {area / 2:.2f} litros de tinta para pintar a parede.')