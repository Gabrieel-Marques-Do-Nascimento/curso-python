numeros = list()
pares = []
impares = []
for c in  range(0,7):
    n = int(input('Digite um numero: '))
    if n % 2 == 0:
        if c == 1 or pares[-1] < n :
            pares.append(n)
        elif pares[0] > n:
            pares.insert(0,n)
    else:
        impares.append(n)
numeros.append(pares)
numeros.append(impares)
print(numeros)