# Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input('Digite um numero: '))
div = 0

for c in range(1,num+1):
    if num%c == 0:
        div += 1
        print('\033[32m',end=' ')
    else:
        print('\033[31m',end=' ')
    print(c,end=' ')
if div == 2:
    tipo = 'E PRIMO!'
else:
    tipo = 'NAO E PRIMO!'
print('\033[0m\nO numero {} foi divisivel por {} vezes'.format(num,div))
print(' por isso ele {}'.format(tipo))

