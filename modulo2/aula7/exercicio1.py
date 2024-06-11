
cont = n = soma = 0
while True:
    n = int(input('Dogite um valor \033[33m[ 999 para parar]\033[m: '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'a soma dos {cont} valores foi {soma}')