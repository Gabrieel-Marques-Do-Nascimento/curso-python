# Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

# lista =[]
# pares = []
# impar = list()
# sn = 's'
# while sn not in 'Nn' :
#     n = int(input('digite um numero: '))
#     lista.append(n)
#     while True:
#        sn= str(input('Quer continuar:[S/N] ')).strip().upper() 
#        if sn[0] in 'SsNs':
#            break
# print(25*'-=')
# print(f'A lista completa e: {lista}')
# for item in lista:
#     if item % 2 == 0: 
#         pares.append(item)
#     else:
#         impar.append(item)
# print(f'A lista de pares e: {pares}')
# print(f'A lista de impares e: {impar}')

# professor

lista =[]
pares = []
impar = list()
while True :
    lista.append(int(input('digite um numero: ')))
    sn= str(input('Quer continuar:[S/N] ')).strip().upper() 
    if sn[0] in 'Nn':
        break
print(25*'-=')
print(f'A lista completa e: {lista}')
for i, v in enumerate(lista):
    if v % 2 == 0: 
        pares.append(v)
    elif v % 2 == 1:
        impar.append(v)
print(f'A lista de pares e: {pares}')
print(f'A lista de impares e: {impar}')