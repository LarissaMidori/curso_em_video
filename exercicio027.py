# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Digite seu nome completo: ')).strip().title()
separar = nome.split()
print(f'Muito prazer em te conhecer {nome}!')
print(f'Seu primeiro nome é: {separar[0]}')
print(f'Seu último nome é: {separar[-1]}')
print(f'Seu último nome é: {separar[len(separar) - 1]}')
