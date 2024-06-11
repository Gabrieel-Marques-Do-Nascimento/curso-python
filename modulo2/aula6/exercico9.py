# Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.


n = 0
c = ''
ct = 0
soma = 0
maior = 0
menor = 0
while c in 'Ss'  :
    n = int(input('digite um valor: '))
    c = str(input('Quer continuar? [S/N] '))
    ct += 1
    soma += n

    if ct == 1:
        maior = n
        menor = n
    if maior <= n:
        maior = n
    if menor >= n:
        menor = n
media = soma/ct
print(f'voce digitol {ct} numeros e a media e {media}')
print(f'o maior numero e {maior} e o menor e {menor}')

# professor 


c = 's'
menor = maior = soma = ct = n = 0
while c in 'Ss'  :
    n = int(input('digite um valor: '))
    c = str(input('Quer continuar? [S/N] ')).strip().upper()
    ct += 1
    soma += n
    if ct == 1:
        maior = n
        menor = n
    else:
        if maior <= n:
            maior = n
        if menor >= n:
           menor = n
media = soma/ct
print(f'voce digitol {ct} numeros e a media e {media}')
print(f'o maior numero e {maior} e o menor e {menor}')
