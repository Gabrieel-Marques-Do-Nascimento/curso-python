#Exercício Python 50: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

soma = 0
for n in range(1,7):
    numero = int(input('{}ᵃ numero '.format(n))) 
    if numero % 2 == 0:
        soma += numero
print(' A soma dos numeros pares e {}'.format(soma))