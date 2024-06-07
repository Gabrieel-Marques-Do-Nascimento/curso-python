'''
Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
'''
num = int(input('digite um numero para ver sua tabuada: '))
cont = 0 
print('-'*12)
print(f'Tabuada de {num}')
print('-'*12)
for t in range(0,10):
    cont+= 1
    print(f'{num} X {cont:2} = {num*cont:2}')
print('-'*12)
