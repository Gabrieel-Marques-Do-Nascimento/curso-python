
from time import sleep

n = mult = 0
while True :
    sleep(.5)
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n <= 0:
        break
    print(34*'-')
    cont = 0
    while cont < 10:
        cont += 1
        mult = n * cont
        sleep(.5)
        print(f'{n} X {cont:2} = {mult:2}')
    print(34*'-')
sleep(.7)
print('FIM')