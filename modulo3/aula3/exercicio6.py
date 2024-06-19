# Exercício Python 087: Aprimore o desafio anterior, mostrando no final:                                                 
#     A) A soma de todos os valores pares digitados.                                                                                          
#     B) A soma dos valores da terceira coluna.                                                                                                              
#     C) O maior valor da segunda linha.

# matris = [[0,0,0],[0,0,0],[0,0,0]]
# par = col3 = mai = 0
# for l in range(0,3):
#     for c in range(0,3):
#         matris[l][c] = int(input(f'Digite um valor para [{l},{c}]: '))
#         if matris[l][c] % 2 == 0:
#             par += matris[l][c]
#         if c == 2:
#             col3 += matris[l][c]
#         if l == 1 and c == 0:
#             mai = matris[l][c]
#         else:
#             if matris[l][c] > mai:
#                 mai = matris[l][c]       
# for l in range(0,3):
#     for c in range(0,3):
#         print(f'[{matris[l][c]:^5}]',end='') 
#     print()
# print(f'A soma dos valores pares e {par}')
# print(f'A soma dos valores da terceira coluna e {col3}')
# print(f'O maior valor da segunda linha e {mai}')

matris = [[0,0,0],[0,0,0],[0,0,0]]
par = col3 = mai = 0
for l in range(0,3):
    for c in range(0,3):
        matris[l][c] = int(input(f'Digite um valor para [{l},{c}]: '))
        if matris[l][c] % 2 == 0:
            par += matris[l][c]
            
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matris[l][c]:^5}]',end='')
       
    print()

print(f'A soma dos valores pares e {par}')
for l in range(0,3):
    col3 += matris[l][2]
print(f'A soma dos valores da terceira coluna e {col3}')
for c in range(0,3):
    if c == 0:
      mai = matris[1][c]
    elif matris[1][c] > mai:
        mai = matris[1][c]
        
print(f'O maior valor da segunda linha e {mai}')