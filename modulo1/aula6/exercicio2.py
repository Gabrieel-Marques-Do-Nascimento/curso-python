'''Exercício Python 23: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

#        usando string  

num = str(input('digite um numro: '))
print(f'Unidade:{num[-1]}')
print(f'Dezena: {num[-2]}')
print(f'Centena:{num[-3]}')
print(f'Milhar: {num[:-3]}')
'''
#          usando numeros
num1 = int(input('digite um numro: '))
u = num1//1%10
d = num1//10%10
c = num1//100%10
m = num1//1000%10
print(f'Unidade:{u}')
print(f'Dezena: {d}')
print(f'Centena:{c}')
print(f'Milhar: {m}')
