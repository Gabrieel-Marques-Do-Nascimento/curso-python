#Exercício Python 16: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua parte  Inteira.
'''
# importando modulo
from math import fabs,trunc

num = float(input('digite um numero: '))
print(f'o numero digitado foi {num} e a sua porcâo  inteira e {trunc(num)}')
'''

#sem import 
num = float(input('digite um numero: '))
print(f'o numero digitado foi {num} e a sua porcao inteira e {int(num)}')

