from random import randint
from time import sleep

mai = 0
lista = []
jogadas = {'jogador1':0,'jogador2':0,'jogador3':0,'jogador4':0}
for k,v in jogadas.items():
    sleep(.7)
    jogadas[k] = randint(1,6)
    lista.append(jogadas[k])
    
    print(f'O {k} tirou {jogadas[k]}')
print(f'<<< Rankng dos Jogadores >>>')
lista.sort(reverse=True)
cont = 0
while len(jogadas) > cont:
    for k,v in jogadas.items():
        if jogadas[k] == lista[cont]:
            sleep(1)
            print(f'{cont+1}ᵒ lugar: {k} com {lista[cont]}') 
            
            
            cont +=1
        if cont == len(jogadas):
            break

    