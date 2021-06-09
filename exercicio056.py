''' Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos. '''

soma = 0
mediaIdade = 0
mulherMenor20 = 0
homemMaisVelho = 0
nomeMaisVelho = ''

for i in range(1, 5):
    print(f'==== Nº {i} ====')
    nome = str(input(f'Nome: ')).strip()
    idade = int(input(f'Idade: '))
    sexo = str(input(f'Sexo: (F para feminino e M para masculino) ')).strip()
    soma += idade
    mediaIdade = soma / i

    if i == 1 and sexo in 'Mm':
        homemMaisVelho = idade
        nomeMaisVelho = nome
    if sexo in 'Mm' and idade > homemMaisVelho:
        homemMaisVelho = idade
        nomeMaisVelho = nome

    if sexo in 'Ff' and idade < 20:
        mulherMenor20 += 1

print(f'A soma das idades é: {soma} e a média das idades é: {mediaIdade:.2f}.')
print(f'O homem mais velho é o {nomeMaisVelho} e ele tem {homemMaisVelho} anos.')
print(f'A quantidade de mulheres menores que 20 anos é: {mulherMenor20}.')
