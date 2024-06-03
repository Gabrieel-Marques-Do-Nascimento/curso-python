#Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

a = float(input('valor 1: '))
b = float(input('valor 2: '))
c = float(input('valor 3: '))

if a + b > c and a + c > b and b + c > a: 
    print(f'os seguimento PODEM FORMAR triangulo')
else:
    print(f'os seguimento NAO PODEM FORMAR triangulo')