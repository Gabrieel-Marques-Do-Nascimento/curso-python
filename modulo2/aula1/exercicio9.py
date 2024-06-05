'''
Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

– EQUILÁTERO: todos os lados iguais

– ISÓSCELES: dois lados iguais, um diferente

– ESCALENO: todos os lados diferentes
'''
t1 = float(input('primeiro segmento: '))
t2 = float(input('Segundo segmento: '))
t3 = float(input('Terceiro segmento: '))

if t1 + t2 > t3 and t1 + t3 > t2 and t2 + t3 > t1:
    if t1 == t2 == t3:
        triangulo = 'EQUILÁTERO'
    elif t1 == t2 or t1 == t3 or t2 == t3:
        triangulo = 'ISÓSCELES'
    else:                              # elif t1 != t2 != t3 != t1:
        triangulo = 'ESCALENO'
    print(f'os segmentos acima podem formar um triangulo', end=' ')
    print(f'{triangulo}!')
else:
     print(f'os segmentos acima nao podem formar um triangulo')