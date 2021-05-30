''' Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez. '''

frase = str(input('Digite uma frase: ')).upper().strip()
separar = frase.split()
juntar = "".join(separar)
print(f'A frase tem {juntar.count("A")} letras A (tanto maiúsculas quanto minúsculas).')
print(f'A primeira letra A aparece na posição {juntar.find("A") + 1} e a última letra A aparece na posição {juntar.rfind("A") + 1}.')
