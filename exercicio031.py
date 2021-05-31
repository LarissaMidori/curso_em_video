''' Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$ 0,50 por Km para viagens de até 200 Km e R$ 0,45 parta viagens mais longas. '''

distancia = float(input('Qual a distância da viagem em Km? '))
print(f'Você está prestes a começar sua viagem de {distancia:.2f} Km.')
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print(f'O valor da passagem é de R$ {preco:.2f}')
