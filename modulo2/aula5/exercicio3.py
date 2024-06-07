'''
Exercício Python 48: Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
'''
s = 0
cont = 0
lista = []
for m3 in range(1,501,2):
    #print('.',end=' ')
    if m3%3 == 0:
      s += m3 # s = s + m3   # acumulador == soma valores
      cont += 1 # contador normalmente soma 1     #lista.append(m3)  
      #print(m3,end=' ')
    
#print(f'a soma de todos os {len(lista)} valores e {s}')
print(f'a soma de todos os {cont} valores e {s}')
