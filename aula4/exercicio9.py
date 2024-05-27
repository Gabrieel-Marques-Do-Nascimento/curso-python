'''
leia o salario e mostre com  15%  de almento '''
salario = float(input('digite o valor do seu salario? '))
aumento = 15
com_aumento = salario+(salario * aumento/100)
print(f'{com_aumento}')