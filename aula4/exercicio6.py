'''
leia quanto dinheiro vc tenha quantos dolares pose comprar   US$ 1,00 = R$ 3.27'''
REAL = int(input('escreva a quantidade que deve ser convertida para dolar: R$'))
valoDolar = 5.16
Iene = 0.0328
Euro = 5.61
print(f'DOLAR US${REAL/valoDolar:.2f}')
print(f'EURO {REAL/Euro:.2f}')
print(f'IENE {REAL/Iene:.2f}')
