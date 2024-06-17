# lista = list()
# cont = 0
# for c in  range(0,5):
#         print(f'digite um numero na {c+1}ᵃ posicao: ',end='')
#         lista.append(int(input())) 
# print(23*'\033[1m-=\033[m')
# # print(f' voce digitou os valores: {lista}')
# print(f'voce digitou os valores: ',end='')
# for y in lista:
#     print(y,end=' ')
# print()
# # print(f'O maior valor digitado foi {max(lista)} nas posicoes {lista.index(max(lista))+1}...')   
# print(f'O maior valor digitado foi {max(lista)} nas posicoes ',end='')  
# for c in lista:
#     cont += 1
#     if max(lista) == c:  
#         print(f'{cont}...',end=' ')
# print()
# cont = 0
# print(f'O menor valor digitado foi {min(lista)} nas posicoes ',end='')
# for i in lista:
#     cont += 1
#     if  min(lista) == i:
#         print(f'{cont}...',end=' ')     
# print('')



# professor

lista = list()
cont = ma = me = 0 
for c in  range(0,5):
        lista.append(int(input(f'digite um numero na {c+1}ᵃ posicao: '))) 
        if c == 0:
            ma = me = lista[c]
        else:
            if lista[c] >= ma:
                ma = lista[c]
            if lista[c] <= me:
                me = lista[c]
        
print(23*'\033[1m-=\033[m')

print(f'voce digitou os valores: {lista}')

print(f'O maior valor digitado foi {ma} nas posicoes ',end='')  
for v, c in enumerate(lista):
    if ma == c:  
        print(f'{v}...',end=' ')
print()
cont = 0
print(f'O menor valor digitado foi {me} nas posicoes ',end='')
for i in lista:
    cont += 1
    if  me == i:
        print(f'{cont}...',end=' ')
print('')
