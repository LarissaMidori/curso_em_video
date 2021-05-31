''' Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80 Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$ 7,00 por cada Km acima do limite. '''

vel = float(input('Digite a velocidade do carro em Km: '))
if vel > 80:
    print(f'Você passou da velocidade limite que é de 80 Km/h e será multado!!')
    print(f'O valor da multa é de: R$ {(vel - 80) * 7:.2f}.')
print(f'Tenha um bom dia e dirija com segurança!')
