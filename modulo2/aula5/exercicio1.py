'''
Exercício Python 46: Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
'''
from time import sleep
from random import randint
num = randint(0,1)
cores = ['\033[1;31m','\033[1;32m']

for laco in range(10,-1, -1):
    sleep(1)
    print(f'{cores[num]}{laco} \033[0m')
print(f"FELIS ANO NOVO")