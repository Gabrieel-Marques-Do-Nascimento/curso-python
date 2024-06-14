# mostrar total gasto  
#q custam mais de 1000
# nome do produto mais barato
# https://www.hashtagtreinamentos.com/formatacao-numerica-no-python

print(35*'-')
print('         LOJA SUPER BARATAO')
print(35*'-')
g =0
soma = cont = menor = 0
nome_barato = ''
while True:
    cont += 1
    nome = str(input('Nome do produto: '))
    preco = float(input('Preco: R$'))
    soma += preco
    if preco > 1000:
        g += 1
    if cont == 1 or preco < menor:
        menor = preco
        nome_barato = nome

    continuar = ' '
    while continuar not in 'SsNn' :
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar in 'Nn':
        break

print('\n{:-^40}\n'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi: R${soma:,.2f}')
print(f'temos {g} produtos custando mais de R$1.000.00')
print(f'O produto mais barato foi: {nome_barato} que custa: R${menor:,.2f}')
