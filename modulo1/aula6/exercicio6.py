# Exercício Python 27: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

# minha resolucao
nome = str(input('Qual o seu nome: ')).split()

print(f'primeiro nome e : {nome[0].capitalize()}\n ultimo nome e {nome[-1].capitalize()}')

# resolucao do professor

n = str(input('Qual o seu nome: ')).strip()
nome = n.split()

print('muito prazer em te conhecer')
print(f'primeiro nome e : {nome[0].capitalize()}\n ultimo nome e {nome[len(nome)-1]}')
