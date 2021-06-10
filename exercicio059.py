''' Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso. '''

from time import sleep

opcao = 0
n1 = int(input('Primeiro nº: '))
n2 = int(input('Segundo nº: '))
while opcao != 5:
    print(f'{"=#" * 16}')
    print(f'''[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa 
''')
    opcao = int(input(f'=== Digite o nº da operação que deseja realizar: '))
    if opcao == 1:
        soma = n1 + n2
        print(f'A soma de {n1} + {n2} é: {soma}.')
    elif opcao == 2:
        produto = n1 * n2
        print(f'A multiplicação de {n1} x {n2} é: {produto}')
    elif opcao == 3:
        if n1 > n2:
            maior = n1
            print(f'O número {maior} é o maior entre {n1} e {n2}.')
        elif n1 < n2:
            maior = n2
            print(f'O número {maior} é o maior entre {n1} e {n2}.')
        else:
            print(f'Os dois nºs são iguais.')
    elif opcao == 4:
        print(f'Digite os novos números:')
        n1 = int(input('Primeiro nº: '))
        n2 = int(input('Segundo nº: '))
    elif opcao == 5:
        print(f'Você está saindo do programa...')
    elif opcao > 5:
        print(f'Opção inválida! Tente novamente.')
sleep(1)       
print(f'Programa finalizado!')
