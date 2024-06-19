lista = [] #[[1],[2],[3],[4],[5],[6],[7],[8],[9]]
item=[]
cont = c0 = c1 =0
'''
for c in range(0,9):
    item.append(int(input(f'Digite um valor para [{c1}] [{c0}]: ')))
    lista.append(item[ ,: ])
    item.clear()
    c0 += 1
    if c0 == 3:
        c0 = 0
        c1 +=1


for v in range(0,9):
    print(lista[v],end=' ')
    cont += 1
    if cont == 3:
        print()
        cont = 0
  '''  '''
for c in range(1,28,3):
    lista.append('[  ')
    lista.append('  ]')
    lista.insert(c,int(input(f'Digite um valor para [{c1}] [{c0}]:')))
    c0 += 1
    if c0 == 3:
        c0 = 0
        c1 +=1
print('\033[1m-=\033[m'*30)
for c in range(0,27):
    print(lista[c],end='')
    cont+=1
    if cont == 9:
        print()
        cont = 0
        
        '''
        # PROFESSOR
        
matris = [[0,0,0],[0,0,0],[0,0,0]]
for l in range(0,3):
    for c in range(0,3):
        matris[l][c] = int(input(f'Digite um valor para [{l},{c}]: '))
print(30*'-=')
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matris[l][c]:^5}]',end='')
    print()