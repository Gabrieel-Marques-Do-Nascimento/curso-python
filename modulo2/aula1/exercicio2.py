#Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

casaValor = float(input('Qual o valor da casa: R$'))
salario = float(input('Qual o seu salario: R$'))
ano = float(input('Quantos anos de financiamento: '))
prestacao = casaValor/(ano*12)

print(f'para pagar uma casa no valor de R${casaValor:.2f} em {ano:.0f} anos')
print(f'a prestacao sera de R${prestacao:.2f}')
if prestacao > salario*30/100 :
    print('Emprestimo Negado')
elif prestacao < salario*30/100:
    print('Emprestimo Aprovado')

# resolucao do professor

casa = float(input('Qual o valor da casa: R$'))
salar = float(input('Qual o seu salario: R$'))
anos = float(input('Quantos anos de financiamento: '))
prestacaes = casa/(anos*12)
mini = salar * 30/100
print(f'para pagar uma casa no valor de R${casa:.2f} em {anos:.0f} anos')
print(f'a prestacao sera de R${prestacaes:.2f}')
if prestacaes > mini :
    print('Emprestimo Negado')
else:
    print('Emprestimo Aprovado')
