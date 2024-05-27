'''
leia um preco de um produto mostre com 5% de desconto'''
produto = float(input('qual o valor? '))
valor = float('0.'+ input('desconto?'))
desconto = produto*valor
print(f'{produto-desconto:.2f} ')