# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

cidade = str(input('Qual o nome da cidade em que você nasceu? ')).strip()
print(f'{cidade[:5].lower() == "santo"}')
