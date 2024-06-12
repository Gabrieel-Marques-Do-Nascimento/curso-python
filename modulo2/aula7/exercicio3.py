from random import randint
print(15*'-=')
print('    VAMOS JOGA PAR OU IMPAR')
print(15*'-=')
soma = cont = cont2  = rs = 0
while True :
    computador = randint(1,10)
    cont2 += 1
    n = int(input('Digite um valor: '))
    soma = n + computador
    escolha = str(input('PAR ou IMPAR? [P/I] ')).strip().upper()[0]
    if escolha in 'PpIi':
        if escolha in 'Pp' and soma % 2 == 0:
            cont += 1
        elif  soma % 2 != 0 and escolha in 'Ii':
            cont += 1  
        else:
            restd = 'VOCE PERDEU!'
        if cont == cont2: restd = 'VOCE VENCEU!\nvamos jogar novamente......'
        rs = 'DEU PAR ' if soma % 2 == 0 else 'DEU IMPAR'
        print(35*'-')
        print(f'voce jogou {n} e o computador {computador}. total de {soma} {rs} ')
        print(35*'-') 
        print(restd) 
        print(18*'=-')  
        if  cont < cont2: break
    else:
        print('\033[33mERRO DIGITE NOVAMENTE\033[m')
print(f'GAME OVER! Voce venceu {cont} vezes')    
