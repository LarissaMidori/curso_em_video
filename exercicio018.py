# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

ang = float(input('Digite um ângulo: '))
print(f'''O ângulo de {ang}° tem:
Cosseno: {math.cos(math.radians(ang)):.2f}
Seno: {math.sin(math.radians(ang)):.2f}
Tangente: {math.tan(math.radians(ang)):.2f}
''')