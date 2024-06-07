'''
inicio = int(input('inicio: '))

fim = int(input('fim: '))

saltar = int(input('saltor: '))

for c in range(inicio,fim, saltar):
    print(c)
print('fim')
'''
#             
s = 0
for c in range(0,3):
    n = int(input('digitem um numero: '))
    s += n # seria tipo isso:  s = s + n
print(f'resultado da soma de todos valores = {s}')
   
