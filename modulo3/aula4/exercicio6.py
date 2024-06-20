pessoas = dict()
lista  = list()
lista = [{'nome': 'gabriel', 'idade': 22, 'Sexo': 'M'}, {'nome': 'camiala', 'idade': 19, 'Sexo': 'F'}, {'nome': 'pedro', 'idade': 15, 'Sexo': 'M'}]
a = media =  0
# while True:
#     pessoas['nome'] = str(input('Nome: ')).strip()
#     pessoas['idade'] = int(input('Idade: '))
#     pessoas['Sexo'] = str(input('Sexo: [M/F] ')).strip().upper()
#     lista.append(pessoas.copy())
#     continuar = str(input('Quer continuar: [S/N] '))[0].strip().upper()
#     cont += 1
#     if continuar in 'Nn':
#         break
print(f'_O grupo tem {len(lista)} Pessoas.')
for i in lista:
    a += i['idade']
media = a/ len(lista)
print(f'_A media de idade e de {media:.2f} anos.')
print(f'_As mulheres cadastradas foram: ',end='')
for i in lista:
    if i['Sexo'] in 'Ff':
        print(i['nome'],end='')
print()
print(f'_lista de pessoas com idade acima da media:')
for i in lista:
    for k,v in i.items():
        if i['idade'] > media:
            print(f'{k} = {v}; ',end='')
    print()
# print(pessoas)   
# print(lista)