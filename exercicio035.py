# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

print(f' {"=#=" * 15}')
print(f'Analisador de triângulos')
print(f' {"=#=" * 15}')
reta1 = float(input('Primeira reta: '))
reta2 = float(input('Segunda reta: '))
reta3 = float(input('Terceira reta: '))
if(reta1 < reta2 + reta3) and (reta2 < reta1 + reta3) and (reta3 < reta1 + reta2):
    print(f'As retas acimas PODEM formar um triângulo')
else:
    print(f'As retas NÃO PODEM formar um triângulo.')
