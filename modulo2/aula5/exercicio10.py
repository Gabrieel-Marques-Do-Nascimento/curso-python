# Exercício Python 55: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
#novalistaRevers = sorted(listnum, reverse=True)          # vai comecar do final  listnum = [1, 2, 3, 4, 5, 6]

maior = 0
menor = 0
for p in range(1,6):
    peso = float(input(f'peso da {p}ᵃ pessoa: ')) 
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
     
print('o menor peso lido foi {}KG e o maior peso lido foi {}KG'.format(menor,maior))        



