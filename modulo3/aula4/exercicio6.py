# pessoas = dict()
# lista  = list()
# #lista = [{'nome': 'gabriel', 'idade': 22, 'Sexo': 'M'}, {'nome': 'camiala', 'idade': 19, 'Sexo': 'F'}, {'nome': 'pedro', 'idade': 15, 'Sexo': 'M'}]
# a = media =  0
# while True:
#     pessoas['nome'] = str(input('Nome: ')).strip()
#     pessoas['idade'] = int(input('Idade: '))
#     pessoas['Sexo'] = str(input('Sexo: [M/F] ')).strip().upper()
#     while pessoas['Sexo'] not in 'MmFf':
#         print('ERRO porfavor digite somente M ou F')
#         pessoas['Sexo'] = str(input('Sexo: [M/F] ')).strip().upper()
#     lista.append(pessoas.copy())
#     continuar = str(input('Quer continuar: [S/N] '))[0].strip().upper()
#     if continuar in 'Nn':
#         break
#     while continuar not in 'SsNn':
#         print('ERRO porfavor digite somente S ou N')
#         continuar = str(input('Quer continuar: [S/N] '))[0].strip().upper()


# print(f'_O grupo tem {len(lista)} Pessoas.')
# for i in lista:
#     a += i['idade']
# media = a/ len(lista)
# print(f'_A media de idade e de {media:.2f} anos.')
# print('_As mulheres cadastradas foram: ',end='')
# for i in lista:
#     if i['Sexo'] in 'Ff':
#         print(i['nome'],end=' ')
# print()
# print('_lista de pessoas com idade acima da media:')
# for i in lista:
#     for k,v in i.items():
#         if i['idade'] > media:
#             print(f'{k} = {v}; ',end='')
#     print()


# professor


pessoas = dict()
lista = list()
# lista = [{'nome': 'gabriel', 'idade': 22, 'Sexo': 'M'}, {'nome': 'camiala', 'idade': 19, 'Sexo': 'F'}, {'nome': 'pedro', 'idade': 15, 'Sexo': 'M'}]
a = media = 0
while True:
    pessoas['nome'] = str(input('Nome: ')).strip()
    pessoas['idade'] = int(input('Idade: '))
    a += pessoas['idade']
    while True:
        pessoas['Sexo'] = str(input('Sexo: [M/F] ')).strip().upper()
        if pessoas['Sexo'] in 'MmFf':
            break
        print('ERRO porfavor digite somente M ou F')
    lista.append(pessoas.copy())
    while True:
        continuar = str(input('Quer continuar: [S/N] '))[0].strip().upper()
        if continuar in 'SsNn':
            break
        print('ERRO porfavor digite somente S ou N')
    if continuar == 'N':
        break


print(f'_O grupo tem {len(lista)} Pessoas.')   
media = a / len(lista)
print(f'_A media de idade e de {media:5.2f} anos.')
print('_As mulheres cadastradas foram: ', end='')
for i in lista:
    if i['Sexo'] == 'F':
        print(i['nome'], end=' ')
print()
print('_lista de pessoas com idade acima da media:')
for i in lista:
    if i['idade'] > media:
        print('     ',end='')
        for k, v in i.items():
            print(f'{k} = {v}; ', end='')
        print()

    # Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
    # A) Quantas pessoas foram cadastradas
    # B) A média de idade
    # C) Uma lista com as mulheres
    # D) Uma lista de pessoas com idade acima da média
