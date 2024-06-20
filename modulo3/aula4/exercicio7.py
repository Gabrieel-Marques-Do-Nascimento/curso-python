def print2(lnh):
    print(30*'-=')
    print(lnh)
    print(30*'-=')

jogador = dict()
gols = list()
jogadores = list()
cont =0 
#jogadores = [{'Name': 'doni', 'Gols': [1, 0, 2, 0], 'Total': 3} , {'Name': 'joao', 'Gols': [3, 0], 'Total': 3} , {'Name': 'Gabriel', 'Gols': [1, 0, 3, 0], 'Total': 4} , {'Name': 'pedro', 'Gols': [1, 0, 2, 0, 1], 'Total': 4}  ]
total = 0
while True:
    jogador['Name'] = str(input('Nome do Jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["Name"]} Jogou? '))
    for c in range(0,partidas):
        gols.append(int(input(f'Quantos Gols na Partida {c}:')))
    jogador['Gols'] = gols[:]
    gols.clear()
    for c in jogador['Gols']:
        total +=c
    jogador['Total'] = total
    total = 0
    jogadores.append(jogador.copy())
    continuar = str(input('Quer continuar: [S/N]')).strip().upper()[0]
    if continuar in 'Nn':
        break

print2(f'{"Cod":<5} {"Nome":<15} {"Gols":>4} {"Total":>20}')
for c in  jogadores:
        print(f'{jogadores.index(c):<5} {c["Name"]:<15} {str(c["Gols"]):20}{c["Total"]}')
    
print()  
# for k,v in jogador.items():
#     print(f'O campo {k} tem o valor {v}.')
print(30*'-=')
while True:
        dados = str(input('Mostrar dados de qual jogador? '))
        print(f'O jogador {jogador["Name"]} jogou {partidas} Partidas.')

