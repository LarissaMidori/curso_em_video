''' Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto. '''

sexo = str(input(f'Informe seu sexo: [F/M] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input(f'Opção inválida! Por favor, informe seu sexo: [F/M] ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso.')
