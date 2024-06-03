#Exercício Python 33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
n1 = int(input('Primeiro numero: '))
n2 = int(input('Segundo numero: '))
n3 = int(input('Terceiro numero: '))

#menor
if n1 < n2 and n1 < n3:
    menor = n1
if n2 < n1 and n2 < n3 :
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
# maior

if n1 > n2 and n1 > n3:
    maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3


print(f'O menor valor digitado foi: {menor}')    
print(f'O maior valor digitado foi: {maior}')  

# resolucao do professor
'''

a = int(input('Primeiro numero: '))
b = int(input('Segundo numero: '))
c = int(input('Terceiro numero: '))

#menor

menor = a
if b < a and b < c :
    menor = b
if c < a and c < b:
    menor = c
# maior

maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c


print(f'O menor valor digitado foi: {menor}')    
print(f'O maior valor digitado foi: {maior}')  

'''