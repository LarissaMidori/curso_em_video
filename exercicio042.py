''' Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

– EQUILÁTERO: todos os lados iguais

– ISÓSCELES: dois lados iguais, um diferente

– ESCALENO: todos os lados diferentes '''

reta1 = int(input('Primeira reta: '))
reta2 = int(input('Segunda reta: '))
reta3 = int(input('Terceira reta: '))
if (reta1 < reta2 + reta3) and (reta2 < reta1 + reta3) and (reta3 < reta1 + reta2):
    if (reta1 == reta2) and (reta1 == reta3):
        triangulo = 'EQUILÁTERO'
    elif(reta1 == reta2) or (reta1 == reta3) or (reta2 == reta3):
        triangulo = 'ISÓSCELES'
    else:
        triangulo = 'ESCALENO'
    print(f'As retas podem formar um TRIÂNGULO {triangulo}.')
else: 
    print(f'As retas NÃO podem formar um TRIÂNGULO.') 
