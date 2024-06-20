def linha(lnh):
    print(30*'-=')
    print(lnh)
    print(30*'-=')

jogador = dict()
gols = list()
total = 0
jogador['Name'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {jogador["Name"]} Jogou? '))
for c in range(0,partidas):
    gols.append(int(input(f'Quantos Gols na Partida {c}:')))
jogador['Gols'] = gols
for c in jogador['Gols']:
    total +=c
jogador['Total'] = total

linha(jogador)
for k,v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print(30*'-=')
print(f'O jogador {jogador["Name"]} jogou {partidas} Partidas.')
for c in range(0,len(jogador['Gols'])):
    print(f'=> Na partida {c}, fes {jogador["Gols"][c]} Gols')
print(f'foi um Total de {jogador["Total"]} de Gols')