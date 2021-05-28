# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

preco = float(input('Qual é o preço do produto? R$ '))
desc = preco - (preco * 5 / 100)
print(f'O preço do produto é R${preco:.2f}, e com o desconto de 5% fica: R${desc:.2f}')