#Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Qual o salario do funcionario: R$'))

if salario <= 1250.00:
    almento = salario * 0.15 # porcentagem
else:
    almento = salario * 10/100  # porcentagem
print(f'Quem ganhava R${salario} passa a ganhar R${salario+almento:.2f} agora')