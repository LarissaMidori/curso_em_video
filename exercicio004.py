''' Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele. '''

algo = input('Digite alguma coisa: ')
print(f'O tipo primitivo desse valor é: {type(algo)}')
print(f'Só tem espaços? {algo.isspace()}')
print(f'É númerico? {algo.isnumeric()}')
print(f'É alfanumérico? {algo.isalnum()}')
print(f'É alfabético? {algo.isalpha()}')
print(f'Tem todas as letras minúsculas? {algo.islower()}')
print(f'Tem todas as letras maiúsculas? {algo.isupper()}')
print(f'Tem a primeira letra maiúscula? "(Está capitalizado?)" {algo.istitle()}')
