''' Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores. '''

from datetime import date

maior = 0
menor = 0
for i in range(1, 8):
    nasc = int(input(f'Digite o {i}º ano de nascimento: '))
    idade = date.today().year - nasc
    if idade >= 18:
        maior += 1
        print(f'A pessoa tem {idade} anos e já atingiu a maioridade.')
        print('')
    else: 
        menor += 1
        print(f'A pessoa tem {idade} anos e ainda não atingiu  a maioridade.')
        print('')
print(f'Temos {maior} pessoa(s) maior(es) de idade. E {menor} pessoa(s) menor(es) de idade.')
