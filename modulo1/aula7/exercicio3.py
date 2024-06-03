'''
Exercício Python 30: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
'''
numero = int(input('digite um numero pra saber se e "par" ou "impar": '))
resto = numero % 2
if resto == 0:
    print('numero e "PAR"')
else:
    print('numero e "IMPAR"')