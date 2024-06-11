# Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

numero =int(input('Numro:'))
cont = 0
result = 0
for n in range(1,11):
   
    if numero % n == 0:
        print('\033[1;31m',end=' ')
        cont += 1
        if cont == 2:
            result = '\033[32m UM NUMERO PRIMO \033[m'
        else:
            result = '\033[1;31m NAO E UM NUMERO PRIMO \033[m'
    else:
        print('\033[1;32m',end=' ')
    print(n,end=' ')
print('\033[m Acabou')
print('O numero {} foi divisivel {} veses'.format(numero,cont))
print('Por isso ele {}!!'.format(result))