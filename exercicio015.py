''' Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado. '''

dias = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos Km foram rodados? '))
pagamento = (dias * 60) + (km * 0.15)
print(f' O carro foi alugado por {dias} dia(s), rodou {km} km e o total a ser pago é: R${pagamento:.2f}.')