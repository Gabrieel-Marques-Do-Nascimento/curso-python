'''Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.'''
num = int(input('Digite um numero: '))

cores = {'vermelho':'\033[7;34;31m','verde':'\033[32m', 'limpo':'\033[m'}

opc = int(input('digite \n1 para binário \n2 para octal \n3 para hexadecimal \nescolha uma opcao de convercao base: '))
if opc == 1:
    bi = bin(num)
    print(f'{num} para binario e {bi[2:]}')
    
    
    
elif opc == 2:
    print(f'octal')
    octal = oct(num)
    print(f'{num} em OCTAL e {octal[2:]}')
    
elif opc == 3:
    hexadecimal = hex(num)
    print(f'{cores["verde"]}{num} em hexadecimal e {hexadecimal[2:]}{cores["limpo"]}')
    
    
    
    
else:
    print(f'{cores["vermelho"]}erro {cores["limpo"]}')