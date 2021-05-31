# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

from datetime import date, datetime

ano = int(input('Digite o ano que quer analisar. Ou coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = datetime.today().year
if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0: # (divisível por 4, mas não por 100) ou divisível por 400
    print(f'O ano {ano} é BISSEXTO.')
else:
    print(f'O ano {ano} NÃO é BISSEXTO')