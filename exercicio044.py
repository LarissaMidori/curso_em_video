''' Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em 2x no cartão: preço normal 

– 3x ou mais no cartão: 20% de juros '''

print(f'{" LOJAS DECOR ":=^40}')
preco = float(input('Valor a ser pago: R$ '))
print(f''' Forma de pagamento:
[1] à vista dinheiro/cheque: 10% de desconto
[2] à vista no cartão: 5% de desconto
[3] em 2x no cartão: preço formal
[4] 3x ou mais no cartão: 20% de juros ''')
opcao = int(input('Digite a opção de pagamento: '))
if opcao == 1:
    pagamento = preco - (preco * 10 / 100)
elif opcao == 2:
    pagamento = preco - (preco * 5 / 100)
elif opcao == 3:
    pagamento = preco
    parcela = pagamento /2
    print(f'Sua compra será parcelada em 2x de R$ {parcela:.2f} sem juros.')
elif opcao == 4:
    vezes = float(input('Dividir em quantas vezes? '))
    pagamento = preco + (preco * 20 / 100)
    parcela = pagamento / vezes
    print(f'Sua compra será parcelada em {vezes:.0f}x de R$ {parcela:.2f} com juros.')
else:
    pagamento = preco
    print(f'Por favor, digite uma opção válida.')
print(f'Sua compra de R$ {preco:.2f}, com a forma de pagamento escolhida vai custar R$ {pagamento:.2f}.')
