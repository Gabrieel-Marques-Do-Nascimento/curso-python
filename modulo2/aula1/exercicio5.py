'''
Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:

– O primeiro valor é maior

– O segundo valor é maior

– Não existe valor maior, os dois são iguais
'''
n1 = int(input('primeiro numero: '))
n2= int(input('segundo numero: '))



if n1 > n2 :
    maior = 'PRIMEIRO valor e maior'
elif n2 > n1 :
    maior = 'SEGUNDO valor e maior'
else:
    maior = 'Não existe valor maior, os dois são iguais'
print(f'{maior}')
    