# Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

n = int(input('Quer a tabuada de que número? '))
print(f'{"=" * 30}')
print(f'A tabuada do número {n} é: ')
print(f'{"=" * 30}')
for i in range(0, 11):
    print(f'{n} X {i} = {n * i}')
print(f'{"=" * 30}')
