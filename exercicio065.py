''' Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores. '''

resposta = 'S'
soma = 0
cont = 0
media = 0
menor = maior = 0
while resposta in 'Ss':
    numero = int(input('Digite um nº: '))
    cont += 1
    soma += numero
    media = soma / cont
    if cont == 1:
        menor = numero
        maior = numero
    else:
        if numero < menor:
            menor = numero
        elif numero > maior:
            maior = numero
    resposta = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
print(f'Você digitou {cont} nºs e a média entre os nºs é: {media:.1f}.')
print(f'O menor valor é {menor} e o maior valor é {maior}.')
