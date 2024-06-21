def print2(lnh):
    """_summary_

    Args:
        lnh (_type_): _description_
        VAI MOSTRAR UMA LINHA ANTES E DOIS DO TESTO
    """
    print(30*'-=')
    print(lnh)
    print(30*'-=')


jogador = dict()
gols = list()
jogadores = list()
cont = 0
# jogadores = [{'Name': 'doni', 'Gols': [1, 0, 2, 0], 'Total': 3}, {'Name': 'joao', 'Gols': [3, 0], 'Total': 3}, {
#    'Name': 'Gabriel', 'Gols': [1, 0, 3, 0], 'Total': 4}, {'Name': 'pedro', 'Gols': [1, 0, 2, 0, 1], 'Total': 4}]
total = 0
while True:
    jogador['Name'] = str(input('Nome do Jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["Name"]} Jogou? '))
    for c in range(0, partidas):
        gols.append(int(input(f'Quantos Gols na Partida {c}:')))
    jogador['Gols'] = gols[:]
    gols.clear()
    for c in jogador['Gols']:
        total += c
    jogador['Total'] = total
    total = 0
    jogadores.append(jogador.copy())
    continuar = str(input('Quer continuar: [S/N]')).strip().upper()[0]
    if continuar in 'Nn':
        break
# ------------------------------------------------------------------------------------------------
# MEU CODIGO

# print2(f'{"Cod":<5} {"Nome":<15} {"Gols":>4} {"Total":>20}')
# for c in jogadores:
#     print(
#         f'{jogadores.index(c):<5} {c["Name"]:<15} {str(c["Gols"]):20}{c["Total"]}')
# print(45*'-')
# ------------------------------------------------------------------------------------------------
# DO PROFESSOR
print(40*'-')
print('cod ',end='')
for y in jogador.keys():
    print(f'{y:<15}',end='')
print()
print(30*'-=')
for k, v in enumerate(jogadores):
    print(f'{k:>3} ', end='')
    for i in v.values():
        print(f'{str(i):<15} ', end="")
    print()
print(30*'-=')

# ------------------------------------------------------------------------------------------------
# meu ciodigo
# while True:
#     dados = int(input('Mostrar dados de qual jogador? '))
#     if dados < len(jogadores):
#         print(f'LEVANTAMENTO DO JOGADOR {jogadores[dados]["Name"]}')
#         for c in jogadores[dados]['Gols']:
#             print(f'No jogo {jogadores[dados]["Gols"].index(c)} fes {c} Gols')
#     elif dados == 999:
#         print('<<< VOLTE SEMPRE >>>')
#         break
#     else:
#         print(
#             f'ERRO nao existe jogador com codigo {dados}! tente novamente ')

# ------------------------------------------------------------------------------------------------
# do professor

while True:
    dados = int(input('Mostrar dados de qual jogador? '))
    if dados == 999:
        print('<<< VOLTE SEMPRE >>>')
        break
    if dados >= len(jogadores):
        print(
            f'ERRO nao existe jogador com codigo {dados}! tente novamente ')
    else:
        print(f'LEVANTAMENTO DO JOGADOR {jogadores[dados]["Name"]}')
        for i, g in enumerate(jogadores[dados]['Gols']):
             print(f'No jogo {i} fes {g} Gols')
