# Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

print('    GERADOR DE PA    ')
print(10*'-=')
_1 = int(input('PRIMEIRO TERMO: '))
razao = int(input('razao da PA: '))
c =0
while c < 10:
    c += 1
    print(_1,end=' → ')
    _1 += razao
print(' FIM')
