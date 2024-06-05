'''
Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço formal 

– 3x ou mais no cartão: 20% de juros
'''

produto = float(input('Valor do Produto: R$'))
pagamento = int(input("""[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] em até 2x no cartão
[ 4 ] 3x ou mais no cartão
FORMA DE PAGAMENTO:"""))
_10porcento = produto*10/100
_5porcennto = produto*5/100
_20porcento = produto*20/100
if pagamento == 1:
    Total = produto-_10porcento # 10% porcento de desconto
elif pagamento == 2:
    Total = produto-_5porcennto
elif pagamento ==3:
    Total = produto
    parcela = Total/2
    print(f'su compra vai ser parcela em 2X de {parcela:.2f} SEM JUROS')
elif pagamento == 4:
    Total = produto+_20porcento
    totalparcela = int(input('Quantas parcelas: '))
    parcela = Total/totalparcela
    print(f'su compra vai ser parcela em {totalparcela}X de {parcela:.2f} COM JUROS')
else:
    Total= 0
    print('OPCAO INVALIDA DE PAGAMENTO [ VOLTAR AO COMECO ]')
print(f'Sua compra de R${produto:.2f} vai custar R${Total:.2f} no final.')
