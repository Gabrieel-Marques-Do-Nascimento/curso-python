# 35 anos de contribuicao
from datetime import date
ano = date.today().year
clt = dict()
clt['Nome'] = str(input('Nome: '))
anonsc = int(input('Ano de nascimento: '))
clt['Idade'] =  ano - anonsc
clt['Ctps'] = int(input('Carteira de Trabalho: [0 nao tem] '))
if clt['Ctps'] > 0:
    clt['Contratacao'] = int(input('Ano de Comtratacao: '))
    clt['Salario'] = float(input('Salario: '))
    clt['Aposentadoria'] = (clt['Idade'] + clt['Contratacao'] + 35) - date.today().year  #clt['Aposentadoria'] = (clt['Contratacao'] - anonsc) + 35
# else:
#     del clt['Ctps']
print(clt)

for k,v in clt.items():
    print(f' - {k } Tem o Valor {v}')