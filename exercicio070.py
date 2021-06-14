''' Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato. '''

print(f' {" LOJA TEM DE TUDO " :-^40}')
total = caro = valorBarato = cont = 0
barato = ' '
while True:
    produto = str(input('Nome do produto: '))
    cont += 1
    preco = float(input('Preço: R$ '))
    total += preco
    if preco > 1000:
        caro += 1
    if cont == 1:
        valorBarato = preco
        barato = produto
    else:
        if preco < valorBarato:
            valorBarato = preco
            barato = produto
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Continuar cadastrando? (S/N) ')).strip().upper()[0]
    if continua == 'N':
        break
print(f'''O total da compra foi de R${total:.2f}. Com {caro} produtos que custam mais de R$ 1000. E com {barato} que foi o produto mais barato, custando R$ {valorBarato:.2f}.''')
print(f'{"-" * 40}')
print(f'OBRIGADO PELA COMPRA! VOLTE SEMPRE!!')
