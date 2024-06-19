# Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,                                      guardando tudo em uma lista. No final, mostre:                                                                                                    A) Quantas pessoas foram cadastradas.                                                                                                                B) Uma listagem com as pessoas mais pesadas.                                                                                                    C) Uma listagem com as pessoas mais leves.
'''
nomeEpeso = []
dados = list()
cont = 0
while True :
    nomeEpeso.append((input('nome: ')))
    nomeEpeso.append(float(input('peso: ')))
    
    dados.append(nomeEpeso[:])
    cont+=1
    nomeEpeso.clear()
    qcont = str(input('Quer continuar: [S/N] '))
    if qcont in 'Nn':
        print(30*'-=')
        break
print(f'Ao todo voce cadastrou {cont} Pessoas.')
peso_menor = peso_maior = dados[0][1]
nome_p_maior = nome_p_menor = 0 
for c in dados:
    if peso_maior < c[1 ]:
        peso_maior = c[1]
    if peso_menor > c[1]:
        peso_menor = c[1]
print(f'O maior peso foi {peso_maior:.1f}kg. peso de ',end='')
for c in dados:
     if peso_maior == c[1]:
         print(f'{c[0]}....',end='')
print()
print(f'O menor peso foi {peso_menor}kg. peso de ',end='')
for c in dados:
    if peso_menor == c[1]:
        print(f'{c[0]}...',end='')
    
  '''  
  
    # PROFESSOR
    
nomeEpeso = []
dados = list()
mai = meno = 0
while True :
    nomeEpeso.append((input('nome: ')))
    nomeEpeso.append(float(input('peso: ')))
    if len(dados) == 0:
        mai = meno = nomeEpeso[1]
    else:
        if nomeEpeso[1] > mai :
            mai = nomeEpeso
        if nomeEpeso[1] < meno :
            meno = nomeEpeso[1]
    dados.append(nomeEpeso[:])
    nomeEpeso.clear()
    qcont = str(input('Quer continuar: [S/N] '))
    if qcont in 'Nn':
        break
print(30*'-=')
print(f'Ao todo voce cadastrou {len(dados)} Pessoas.')
print(f'O maior peso foi {mai:.1f}kg. peso de ',end='')
for p in dados:
   if  p[1] == mai:
        print(f'[{p[0]}]',end=' ')
print()
print(f'O menor peso foi {meno}kg. peso de ',end='')
for p in dados:
   if  p[1] == meno:
        print(f'[{p[0]}]',end=' ')
print()