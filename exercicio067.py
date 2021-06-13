''' Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo. '''

while True:
    num = int(input('Quer ver a tabuada de que nº? '))
    print(f'{"=" * 30}')
    if num < 0:
        break
    print(f' A tabuada do {num} é: ')
    for cont in range(1, 11):
        print(f'{num} x {cont} = {num * cont}')
    print(f'{"=" * 30}')
print('Programa finalizado. Tenha um bom dia!')
