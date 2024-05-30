'''Exercício Python 20: O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.'''

from random import shuffle

l1 = str(input('primeiro Aluno: '))
l2 = str(input('Segundo Aluno: '))
l3 = str(input('Terceiro Aluno: '))
l4 = str(input('Quarto Aluno: '))
alunos = [l1, l2, l3, l4]

shuffle(alunos)
print(f'Ordem de Apresentacao do trabalho e {alunos}')