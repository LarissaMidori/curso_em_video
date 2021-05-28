# Escreva um programa que leia uma temperatura digitada em °C e converta para °F

temp = float(input('Digite a temperatura em °C: '))
print(f'A temperatura de {temp:.1f}°C, equivale à {(temp * 1.8 + 32):.1f}°F.')