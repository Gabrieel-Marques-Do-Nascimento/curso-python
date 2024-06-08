#Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date

ms18 = 0
mn18 = 0
anoat = date.today().year
for d in range(1,8):
    datansc = int(input('Data de Nascimento da {}ᵃ pessoa : '.format(d)))  
    if anoat-datansc >= 18:
        ms18 += 1
    elif anoat - datansc < 18: 
        mn18 += 1
print('\nao todo tivemos {} maiores de idade \ne tambem tivemos {} menores de idade\n'.format(ms18,mn18))