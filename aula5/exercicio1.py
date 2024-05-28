#Exercício Python 16: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
from math import fabs,trunc

num = float(input('digite um numero: '))
print(f'o numero digitado foi {num} e a sua porcâo  inteira e {trunc(num)}')


