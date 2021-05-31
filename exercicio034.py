''' Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$ 1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%. '''

salario = float(input('Qual o valor do salário em R$? '))
if salario > 1250:
    aumento = 10
    salarioMaior = salario + (aumento * salario / 100)
else:
    aumento = 15
    salarioMaior = salario + (aumento * salario / 100)
print(f'O salário de R$ {salario:.2f} com o aumento de {aumento}% fica R$ {salarioMaior:.2f}')
