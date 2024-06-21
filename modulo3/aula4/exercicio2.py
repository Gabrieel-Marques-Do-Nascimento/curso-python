
from random import randint
from operator import itemgetter
from time import sleep


# mai = 0
# lista = []
# jogadas = {'jogador1': 0, 'jogador2': 0, 'jogador3': 0, 'jogador4': 0}
# for k, v in jogadas.items():
#     sleep(.7)
#     jogadas[k] = randint(1, 6)
#     lista.append(jogadas[k])

#     print(f'O {k} tirou {jogadas[k]}')
# print('<<< Rankng dos Jogadores >>>')
# lista.sort(reverse=True)
# cont = 0
# while len(jogadas) > cont:
#     for k, v in jogadas.items():
#         if jogadas[k] == lista[cont]:
#             sleep(1)
#             print(f'{cont+1}ᵒ lugar: {k} com {lista[cont]}')

#             cont += 1
#         if cont == len(jogadas):
#             break


mai = 0
lista = []
jogadas = {'jogador1': randint(1, 6),
           'jogador2': randint(1, 6),
           'jogador3': randint(1, 6),
           'jogador4': randint(1, 6)}
ranking = list()
print('valores sorteados: ')
for k,v in jogadas.items():
    print(f'O {k} tirou {jogadas[k]}')
    sleep(1)
ranking = sorted(jogadas.items(), key=itemgetter(1), reverse=True)
print('<<< Rankng dos Jogadores >>>')
for i,v in enumerate(ranking):
    sleep(1)
    print(f'{i+1}ᵒ lugar: {v[0]} com {v[1]}')
