''' Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o. '''

par = 0
cont = 0
for i in range(1, 7):
    num = int(input(f'Digite o {i}º: '))
    if num % 2 == 0:
        par += num
        cont += 1
print(f' A soma do(s) {cont} número(s) par(es) é: {par}.')
