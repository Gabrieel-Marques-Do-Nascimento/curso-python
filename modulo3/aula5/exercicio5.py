from random import randint
from time import sleep


def sorteion5(lista):
    for cont in range(0, 5):
        lista.append(randint(1, 10))
    print('Sorteando 5 numeros da lista', end='')
    for c in lista:
        sleep(.7)
        print(F' {c} ', end='', flush=True)
    sleep(.5)
    print('PRONTO!!')


def somar(lista):
    s = 0
    for c in lista:
        if c % 2 == 0:
            s += c
    print(f'somando os valores pares de {lista} temos {s}')


a = []
numm = list()
sorteion5(numm)
somar(numm)
