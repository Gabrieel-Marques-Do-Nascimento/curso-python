# Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:
# 1 + 1 = 2 + 1  =  3 + 2 = 5 + 3 = 8 + 5 = 13...........
# 0 – 1 – 1 – 2 – 3 – 5 – 8
print(26*'=')
print('  Sequência de Fibonacci ')
print(26*'=')
n = int(input('Quantos termos voce quer: '))
cont = 3
t1 = 0
t2 =1
print(f'{t1} → {t2} ',end='')
while n >= cont:
    t3 = t1 + t2
    print(f'→ {t3} ',end='')
    t1 = t2
    t2 = t3
    cont += 1