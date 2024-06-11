# Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).






# c = False
# soma = cont = 0
# while not c:
#     n =  int(input('Digite um numero inteiro [ 999 PARAR]: '))
#     if n != 999:
#         cont += 1
#         soma = soma + n
#     else:
#         c =True
# print(f'VOCE DIGITOU {cont} ITENS E A SOMA DESSES VALORES E {soma}')

     # PROFESSOR    
 
cont = 0
soma = 0
n =  int(input('Digite um numero inteiro [ 999 PARAR]: '))
while n != 999:
    cont += 1
    soma = soma + n
    n =  int(input('Digite um numero inteiro [ 999 PARAR]: '))
print(f'VOCE DIGITOU {cont} ITENS E A SOMA DESSES VALORES E {soma}')