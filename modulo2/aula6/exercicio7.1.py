n = int(input('Digite a quantidade de valores que voce quer: '))
cont = 3
t1 = 0
t2 = 1
print(f'{t1} → {t2} → ',end='')
while cont <= n:
    t3 = t1 + t2
    print('{} → '.format(t3),end='')
    cont += 1
    t1 = t2
    t2 = t3 
print(' FIM ')
   