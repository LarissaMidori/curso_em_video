''' Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

– IMC abaixo de 18,5: Abaixo do Peso

– Entre 18,5 e 25: Peso Ideal

– 25 até 30: Sobrepeso

– 30 até 40: Obesidade

– Acima de 40: Obesidade Mórbida '''

peso = float(input('Peso em kg: (Exemplo: 78.5) '))
altura = float(input('Altura em m: (Exemplo: 1.75) '))
imc = peso / (altura * altura)
if imc < 18.5:
    faixa = 'ABAIXO DO PESO'
elif imc >= 18.5 and imc < 25:
    faixa = 'PESO IDEAL'
elif imc >= 25 and imc < 30:
    faixa = 'SOBREPESO'
elif imc >= 30 and imc < 40:
    faixa = 'OBESIDADE'
else:
    faixa = 'OBESIDADE MÓRBIDA'
print(f'''Seu peso é {peso:.1f} kg e sua altura é {altura:.2f} m. 
O IMC é {imc:.1f} e sua faixa é: {faixa}.''')
