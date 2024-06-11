
from random import randint
print(15*'-=')
print('    VAMOS JOGA PAR OU IMPAR')
print(15*'-=')

soma = 0
while True :
    computador = randint(1,10)
    n = int(input('Digite um valor: '))
    soma = n + computador
    escolha = str(input('PAR ou IMPAR? [P/I] '))
    
    
    