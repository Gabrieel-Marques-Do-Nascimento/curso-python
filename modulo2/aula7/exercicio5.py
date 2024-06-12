# mostrar total gasto  
#q custam mais de 1000
# nome do produto mais barato

print(35*'-')
print('         LOJA SUPER BARATAO')
print(35*'-')
g =0
soma = 0
while True:
    nome = str(input('Nome do produto: '))
    preco = int(input('Preco: R$'))
    soma += preco
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    while continuar not in 'SsNn' :
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    if continuar in 'Nn':
        break
    
print('\n--------- FIM DO PROGRAMA ----------\n')
print('O total da compra foi: ')
print('temos {} produtos custando mais de R$1.000')
print('O produto mais barato foi {} que custa{}')
