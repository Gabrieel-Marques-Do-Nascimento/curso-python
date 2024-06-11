# Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.



# print('    GERADOR DE PA    ')
# print(10*'-=')
# _1 = int(input('PRIMEIRO TERMO: '))
# razao = int(input('razao da PA: '))
# fim = False
# c=0
# cont = 0
# while not fim :
    
#     while c < 10:
#         cont += 1
#         print(_1,end=' → ')
#         _1 += razao
#         c = c + 1
#     print('PAUSA')
#     d = 0
#     termoeExtra = int(input('mais quantos termos: '))
#     while d < termoeExtra:
#         cont = cont + 1
#         d+=1
#         _1+= razao 
#         print(_1,end=' → ')
#     if termoeExtra == 0:
#         fim = True
# print('progrecao finalizada com {} termos mostrados'.format(cont))


# professor

print('    GERADOR DE PA    ')
print(10*'-=')
_1 = int(input('PRIMEIRO TERMO: '))
razao = int(input('razao da PA: '))
c =0
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while c < total:
        c += 1
        print(_1,end=' → ')
        _1 += razao
    print('PAUSA')
    mais = int(input('mais quantos termos: '))
print(' FIM')
print('progrecao finalizada com {} termos mostrados'.format(c))