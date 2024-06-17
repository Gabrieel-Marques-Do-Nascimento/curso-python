nomeEpeso = []
dados = list()
cont = 0
while True :
    nomeEpeso.append((input('nome: ')))
    nomeEpeso.append(float(input('peso: ')))
    qcont = str(input('Quer continuar: [S/N] '))
    dados.append(nomeEpeso[:])
    cont+=1
    nomeEpeso.clear()
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
    