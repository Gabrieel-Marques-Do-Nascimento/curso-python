# Exercício Python 17: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

# forma matematica  
'''
oposto = float(input('qual e o comprimento do cateto oposto: '))
adjasente = float(input('qual o comprimento do cateto adjasente: '))
hipotenusa =  (oposto**2 + adjasente**2)**(1/2)
print(f'{hipotenusa:.2}')  '''

# com import 

from math import hypot 
oposto = float(input('qual e o comprimento do cateto oposto: '))
adjasente = float(input('qual o comprimento do cateto adjasente: '))
hipotenusa = hypot(oposto,adjasente)
print(f'a hipotenuza e {hipotenusa:.2}')