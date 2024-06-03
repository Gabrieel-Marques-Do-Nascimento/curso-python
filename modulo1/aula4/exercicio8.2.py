produto = float(input('qual o valor? '))
valor = float(input('desconto?'))
desconto = produto - (produto * valor / 100)
print(f'{desconto:.2f} ')