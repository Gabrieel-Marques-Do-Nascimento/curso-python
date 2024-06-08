#Exercício Python 50: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

par = 0
cont = 0
for p in range(1,7):
    num = int(input('digite o {} valor: '.format(p)))
    if num % 2 == 0:
        par += num
        cont += 1
print('voce informou {} numeros pares e a soma foi {}'.format(cont,par))