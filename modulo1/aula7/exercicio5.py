# Exercício Python 32: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
from datetime import date 

ano = int(input('Qual ano quer analizar? 0 para analizar o ano atual:'))
bissexto = ano % 4
if ano ==0:
    ano = date.today().year # pega o ano atual da maquina
if ano % 4 == 0 and ano % 100 != 0  or ano % 400 == 0:
   print(f"Ano de {ano} e bissexto")
else:
   print(f'Ano de {ano} nao e bissexto')
