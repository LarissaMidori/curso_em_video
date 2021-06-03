''' Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 
1 para binário, 2 para octal e 3 para hexadecimal. '''

print(f'{"=**=" * 15}')
print(f'CONVERSOR DE BASES NUMÉRICAS: ')
print(f'{"=**=" * 15}')
num = int(input(' Digite um número inteiro: '))
print(f''' Escolha umas das opções para converter:
1 - converter para BINÁRIO
2 - converter para OCTAL
3 - converter para HEXADECIMAL ''')
base = int(input('Digite sua opção: '))
if base == 1:
    print(f'O número {num} convertido para BINÁRIO vale {bin(num)[2:]}') #[2:] fatia os 2 primeiros índices da string
elif base ==2:
    print(f'O número {num} convertido para OCTAL vale {oct(num)[2:]}')
elif base == 3:
    print(f'O número {num} convertido para HEXADECIMAL vale {hex(num)[2:]}')
else:
    print(f'Opção inválida! Por favor, tente novamente.')
