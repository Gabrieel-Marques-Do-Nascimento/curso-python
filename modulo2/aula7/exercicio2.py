
from time import sleep

n = mult = 0
while True :
    sleep(.5)
    n = int(input('Quer ver a tabuada de qual valor? '))
    print(34*'-')
    if n <= 0:
        break
    for c in range(1,11):
        mult = n * c
        sleep(.5)
        print(f'{n} X {c:2} = {mult:2}')
    print(34*'-')
sleep(.7)
print('FIM')