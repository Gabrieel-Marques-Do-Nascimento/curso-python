'''
Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.
'''
from time import sleep
from random import randint
'''print("""Suas opcoes:
[ 1 ] PEDRA
[ 2 ] PAPEL 
[ 3 ] TESOURA""")
escolha = int(input('Qual a sua jogada? '))
aleatorio = randint(1,3) 
cores = {'limpa':'\033[m','vermelho':'\033[4;31m','VERDE':'\033[1;32m','azul':'\033[1;34m'}
if escolha == 1 or escolha == 2 or escolha == 3:
    if escolha == 1:
        jogador = 'PEDRA'
        if aleatorio == 1:
            comp = 'PEDRA'
            result = '\033[1;34mEMPATE\033[m'
        elif aleatorio == 2:
            comp ='PAPEL'
            result = '\033[4;31mCOMPUTADOR VENCE\033[m'
        elif aleatorio == 3:
            comp = 'TESOURA'
            result = '\033[1;32mJOGADOR VENCE\033[m'
    elif escolha == 2:
        jogador = 'PAPEL'
        if aleatorio == 1:
          comp = 'PEDRA'
          result = '\033[1;32mJOGADOR VENCE\033[m'
        elif aleatorio == 2:
           comp = 'PAPEL'
           result = '\033[1;34mEMPATE\033[m'
        elif aleatorio == 3:
             comp = 'TESOURA'
             result = '\033[4;31mCOMPUTADOR VENCE\033[m'
    elif escolha == 3:
        jogador = 'TESOURA'
        if aleatorio == 1:
            comp = ' PEDRA'
            result = '\033[4;31mCOMPUTADOR VENCE\033[m'
        elif aleatorio ==  2:
            comp = 'PAPEL'
            result = '\033[1;32mJOGADOR VENCE\033[m'
        elif aleatorio == 3:
            comp = 'TESOURA'
            result = '\033[1;34mEMPATE\033[m'
    sleep(.8)
    print('JO')
    sleep(.8)
    print('KEN')
    sleep(.8)
    print('PO!!!')
    print(12*'-=')
    print(f'Computador Jogou {comp}')
    print(f'Jogador Jogou {jogador}')
    print(12*'-=')
    print(f'{result}')
else:
    print(f'OPCAO {cores["vermelho"]} {escolha} {cores["limpa"]} INVALIDA')
    sleep(.5)
    print(f'{cores["vermelho"]}E R R O ! {cores["limpa"]}')
    sleep(.6)
    print(f'{cores["vermelho"]}E R R O !! {cores["limpa"]}')
    sleep(.8)
    print(f'{cores["vermelho"]}E R R O !!!{cores["limpa"]}')
    sleep(.5)
    print('\033[1m**TENTE DIGITAR UMA OPCAO VALIDA**')'''
    
    # resolucao do professor
print("""Suas opcoes:
[ 0 ] PEDRA
[ 1 ] PAPEL 
[ 2 ] TESOURA""")
escolha = int(input('Qual a sua jogada? '))
itens = ('PEDRA','PAPEL','TESOURA')
computador = randint(0,2) 
result = 0
jogador = itens[escolha]
cores = {'limpa':'\033[m','vermelho':'\033[4;31m','VERDE':'\033[1;32m','azul':'\033[1;34m'}

if computador == 0: # computador jogou PEDRA
    if escolha == 0:
        result = 'ENPATE'
    elif escolha == 1:
        result = 'jogador VENCE'
    elif escolha == 2:
        result = 'COMPUTADOR VENCE'
    else:
        print(f'OPCAO {cores["vermelho"]} {escolha} {cores["limpa"]} INVALIDA')
        sleep(.5)
        print(f'{cores["vermelho"]}E R R O ! {cores["limpa"]}')
        sleep(.6)
        print(f'{cores["vermelho"]}E R R O !! {cores["limpa"]}')
        sleep(.8)
        print(f'{cores["vermelho"]}E R R O !!!{cores["limpa"]}')
        sleep(.5)
        print('\033[1m**TENTE DIGITAR UMA OPCAO VALIDA**')
elif computador == 1: # computador jogou PAPEL
    if escolha == 0:
        result = 'COMPUTADOR VENCE'
    elif escolha == 1:
          result = 'ENPATE'
    elif escolha == 2:
          result = 'jogador VENCE'
    else:
        print(f'OPCAO {cores["vermelho"]} {escolha} {cores["limpa"]} INVALIDA')
        sleep(.5)
        print(f'{cores["vermelho"]}E R R O ! {cores["limpa"]}')
        sleep(.6)
        print(f'{cores["vermelho"]}E R R O !! {cores["limpa"]}')
        sleep(.8)
        print(f'{cores["vermelho"]}E R R O !!!{cores["limpa"]}')
        sleep(.5)
        print('\033[1m**TENTE DIGITAR UMA OPCAO VALIDA**')
elif computador == 2: # computador jogou TESOURA
    if escolha == 0:
          result = 'jogador VENCE'
    elif escolha == 1:
          result = 'COMPUTADOR VENCE'
    elif escolha == 2:
        result = 'ENPATE'
    else:
        print(f'OPCAO {cores["vermelho"]} {escolha} {cores["limpa"]} INVALIDA')
        sleep(.5)
        print(f'{cores["vermelho"]}E R R O ! {cores["limpa"]}')
        sleep(.6)
        print(f'{cores["vermelho"]}E R R O !! {cores["limpa"]}')
        sleep(.8)
        print(f'{cores["vermelho"]}E R R O !!!{cores["limpa"]}')
        sleep(.5)
        print('\033[1m**TENTE DIGITAR UMA OPCAO VALIDA**')

sleep(.8)
print('JO')
sleep(.8)
print('KEN')
sleep(.8)
print('PO!!!')
print(12*'-=')
print(f'Computador Jogou {itens[computador]}')
print(f'Jogador Jogou {jogador}')
print(12*'-=')
print(f'{result}')