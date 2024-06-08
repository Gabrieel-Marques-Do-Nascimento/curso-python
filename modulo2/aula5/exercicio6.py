#Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

print(28*'=')
print(F'    10 TERMOS DE UMA PA')
print(28*'=')
_1_termo = int(input('Primeiro Termo: '))
rasao = int(input('Rasao: '))
decimo = _1_termo + (10 - 1) * rasao
for pr in range(_1_termo ,decimo+ rasao, rasao):
    
    print('{:2}'.format(pr),end=' ➔ ')
print(' Acabou')