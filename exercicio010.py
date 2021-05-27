# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares, euros ou ienes ela pode comprar

dinheiro = float(input('Quanto dinheiro você tem na carteira? R$ '))
print(f'''Com {dinheiro:.2f} reais, você pode comprar:
 {dinheiro / 5.24:.2f} dólares
 {dinheiro / 6.39:.2f} euros
 {dinheiro / 0.048:.2f} ienes
 ''')
