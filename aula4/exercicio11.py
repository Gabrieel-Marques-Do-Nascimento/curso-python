#Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

aluguel_dia = 60
valor_km = 0.15
dias = float(input('voce alugou o carro por quantos dias: '))
km = float(input('quantos km voce rodou: '))
print(f'R${(dias*aluguel_dia)+(km*valor_km)}')

