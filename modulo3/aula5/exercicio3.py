from time import sleep


def contagen():

    print(20*'-=')
    print('contagem de 1 ate 10 de 1 em 1')
    for c in range(1, 11, 1):
        sleep(.5)
        print(c, end=' ')
        sleep(.5)
    print('FIM!')
    print(20*'-=')
    print('contagem de 10 ate 0 de 2 em 2')
    for c in range(10, -1, -2):
        sleep(.5)
        print(c, end=' ')
        sleep(.5)
    print('FIM!')
    print(20 * '-=')
    print('A gora e sua vez de personalizar a contagem!!')
    i = int(input('inicio: '))
    f = int(input('fim: '))
    p = int(input('salto: '))
    if p == 0:
        p = 1
    if i > f:
        p = -1 * p
        f-=1
    if i < f :
        f +=1
        if p < 0:
            p = abs(p)
    for c in range(i, f, p):
        sleep(.6)
        print(c, end=' ')
        sleep(.6)
    print('FIM!')


# contagen(,,)
contagen()
