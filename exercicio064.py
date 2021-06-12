''' Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag). '''

digitados = 0
soma = 0
n = int(input('Digite um nº: [999 para parar] '))
while n != 999:
    digitados += 1
    soma += (n)
    n = int(input('Digite um nº: [999 para parar] '))
print(f'Foram digitados {digitados} nºs e o total da soma deles é {soma}.')
