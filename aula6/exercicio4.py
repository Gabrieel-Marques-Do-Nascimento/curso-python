# Exercício Python 25: Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

name = str(input('Qual o seu nome: ')).strip()
silva = 'silva' in name.lower()
print(f'seu nome tem silva: {silva}')