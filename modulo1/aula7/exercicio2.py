'''
Exercício Python 29: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
'''
velocidade = int(input('Qual a velocidade atual do Carro? '))
veloMAX = 80
multaKM = 7.00
multa = (velocidade - veloMAX)*multaKM
if velocidade > veloMAX:
    print(f'MULTADO! voce excedeu o limite permitido que e {veloMAX}Km/h,')
    print(f'voce deve pagar uma multa de R${multa}!')


print('TENHA UM BOM DIA!  DIRIJA COM SEGURANCA! ')