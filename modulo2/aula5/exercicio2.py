'''
Exercício Python 47: Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 51.

#resto = num = int(1) %2

for par in range(0,51,2):
    print(par)


for par2 in range(0,51):
    resto = par2 %2
    if resto == 0:
       print(par2)
  '''    
  
  
''' 
#  add cada numero do for a uma lista 
 
lista = []  
for par3 in range(0,51,2):
    lista.append(par3)
    
'''
for v in range(2,51,2):
    print(v, end=' ')
