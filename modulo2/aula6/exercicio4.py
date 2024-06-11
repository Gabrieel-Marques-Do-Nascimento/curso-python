# Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:

# 5! = 5 x 4 x 3 x 2 x 1 = 120


num = int(input('Digite um numero para\ncalcular a fatorial? '))
c = num
f = 1
print('Calculando {}! = '.format(num),end='')
while c > 0 :
        print('{}'.format(c), end='')
        
        print(' X ' if c > 0 else ' = ', end='')
        f *= c # f  igual f vezes c a cada execucao c tira 1.. ex : f1 X c5 , f5 X c4 , f20 X c3 , f60 X c2 == f120 resultado da fatorial de 5
        c -= 1  # c - 1 
        
print('= {}'.format(f))
