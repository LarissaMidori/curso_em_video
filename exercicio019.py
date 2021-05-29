''' Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo os nomes dos alunos e escrevendo na tela o nome do escolhido. '''

from random import choice

n1 = input('Primeiro nome: ')
n2 = input('Segundo nome: ')
n3 = input('Terceiro nome: ')
n4 = input('Quarto nome: ')
alunos = [n1, n2, n3, n4]
print(f'O sorteado foi: {choice(alunos)}')
