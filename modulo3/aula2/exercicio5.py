# Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.                  Depois disso, mostre:                                                                                                                                                A) Quantos números foram digitados.                                                                                                                    B) A lista de valores, ordenada de forma decrescente.                                                                                          C) Se o valor 5 foi digitado e está ou não na lista.


# lista = []
# sn = ' '
# cont = 0
# while True:
    
#     if sn[0] in 'Ss' or cont == 0:
#         cont += 1
#         print(f'Digite o {cont}ᵃ numero: \033[30m',end='') 
#         n = int(input(''))
#         print('\033[m',end='')
#         lista.append(n)
#     elif sn[0] in 'Nn':
#         print('falow')
#         break
#     sn = str(input('Quer continuar: [S/N]')).strip().upper()
# print(f'foram digitados {cont} numeros')
# lista.sort(reverse=True)
# print(f'os valores em ordem decrecente: {lista}')
# cont = 'nao fas'
# for item in lista:
#     if item == 5:
#         cont = 'fas'
# print(f'o valor 5 {cont} parte da lista!!')        


# professor
lista = []
sn = ' '
cont = 0
while True: 
    if sn[0] in 'Ss' or cont == 0:
        cont += 1
        print(f'Digite o {cont}ᵃ numero: \033[30m',end='') 
        n = int(input(''))
        print('\033[m',end='')
        lista.append(n)
    elif sn[0] in 'Nn':
        print('falow')
        break
    sn = str(input('Quer continuar: [S/N]')).strip().upper()
print(f'foram digitados {len(lista)} numeros')
lista.sort(reverse=True)
print(f'os valores em ordem decrecente: {lista}')
if 5 in lista:
        cont = 'fas'
else:
    cont = 'nao fas'
print(f'o valor 5 {cont} parte da lista!!') 