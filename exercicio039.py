''' Faça um programa que leia o sexo da pessoa, se for feminino diga que não precisa se alistar, senão, se for masculino peça o ano de nascimento e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo. '''

from datetime import date

sexo = str(input('Qual seu sexo? Digite M para masculino ou F para feminino: ')).upper()
if sexo == 'F':
    print(f'Você não precisa se alistar.')
elif sexo == 'M':
    ano = int(input(f'Ano de nascimento: '))
    idade = (date.today().year) - ano
    if idade == 18:
        print(f'Você tem {idade} anos e está na idade para se alistar!')
    elif idade < 18:
        print(f'''Você tem {idade} anos e ainda falta(m) {18 - idade} ano(s) para se alistar.
Seu alistamento será em {ano + 18}.''')
    elif idade > 18:
        print(f'''Você tem {idade} anos e já passaram-se {idade - 18} anos da idade para se alistar.
A idade para se alistar foi em {ano + 18}.''')
else:
    print(f'Por favor, digite uma opção válida!')
    