''' 
Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.'''
from random import randint
from time import sleep
computador= randint(0,5)
print('-=-'*20)
print('vou pencar em um numero entre 0 e 5, tenet adivinhar....')
print('-=-'*20)
jogador = int(input('adivinhe qual e o numero: '))
print('procecando...')
sleep(2.5)
if computador == jogador:
    print('Asertou Miseravi! ksksksk')
else:
    print('errou!')   
print(f'eu escolhi {computador}  ')
# print(computador)