''' Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos. '''

print(f' === Cadastro de pessoas ===')
idade = maior= homem = mulherMenos20 = pessoas = 0
while True:
    idade = int(input('Idade: '))
    pessoas += 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: (F/M) ')).strip().upper()[0]
    if idade > 18:
        maior += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulherMenos20 += 1
    continua = ' '
    print(f'------')
    while continua not in 'SN':
        continua = str(input('Quer continuar? (S/N) ')).strip().upper()[0]
    print(f'------')
    if continua == 'N':
        break
print(f''' 
Temos o total de {pessoas} pessoas cadastradas e:
{maior} pessoas com mais de 18 anos;
{homem} homens;
{mulherMenos20} mulheres com menos de 20 anos. ''')
