from random import randint
from time import sleep
# jogo = list()
# cc = n = 0
# print('\033[1m-\033[m'*35)
# print(f"{'JOAGA NA MEGA SENA':^35}")
# print('\033[1m-\033[m'*35)
# cont = int(input('Quantos jogos voce quer que eu sorteie? '))
# print(f'\033[1m-=-=-=-=-= SORTEANDO {cont} JOGOS! -=-=-=-=-=\033[m')
# for c in range(0,cont):
#     cc = 6
#     for g in range(0,cc):
#         n = randint(0,60)
#         if n in jogo:
#             cc += 1
#         else:
#             jogo.append(n)
#     sleep(.5)
#     print(f'jogo {c+1}: {jogo}')
#     sleep(.5)
#     jogo.clear()
# print(f'\033[1m-=-=-=-=-= < BOA SORTE! > -=-=-=-=-=\033[1m')

# professor
jogo = list()
lista = []
print('\033[1m-\033[m'*35)
print(f"{'JOAGA NA MEGA SENA':^35}")
print('\033[1m-\033[m'*35)

tot = 0
quant = int(input('Quantos jogos voce quer que eu sorteie? '))
while tot <+ quant:
    cont = 1
    while True:
        n = randint(0,60)
        if n not in jogo:
            jogo.append(n)
        if cont == 6:
            break
        cont+=1
    jogo.sort()
    lista.append(jogo[:])
    jogo.clear()
    tot += 1
print(f'\033[1m-=-=-=-=-= SORTEANDO {cont} JOGOS! -=-=-=-=-=\033[m')
for i, l in enumerate(lista):
    print(f'jpgo {i+1}: {l}')