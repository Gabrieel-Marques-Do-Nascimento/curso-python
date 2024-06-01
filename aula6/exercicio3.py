'''
Exercício Python 24: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.
'''
cdd = str(input('diga o nome da sua cidade: ').upper())
cidade = cdd.split()
santa = cidade[0]
vdd = 'SANTA' in santa
print(vdd)

#resolucao do professor

cdd1 = str(input('diga o nome da sua cidade: ')).strip()

print(cdd1[:5].upper()=='SANTA')

