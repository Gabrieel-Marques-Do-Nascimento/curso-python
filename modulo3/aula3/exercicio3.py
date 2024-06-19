'''
numeros = []
pares = [] 
impares = []

cont = 0
v = 0
for c in  range(0,7):
    n = int(input('Digite um numero: '))
    if n % 2 == 0:
        if v == 0 or pares[-1] < n :
            pares.append(n)
        else:
            pos = 0
            while pos < len(pares):
                if pares[pos] >= n:
                    pares.insert(pos,n)
                    break
                pos += 1
        v += 1
    else:
        if cont == 0 or impares[-1] < n:
            impares.append(n)
        else:
            pos = 0
            while pos < len(impares):
                if impares[pos] >= n:
                    impares.insert(pos,n)
                    break
                pos += 1
        cont += 1
numeros.append(pares)
numeros.append(impares)
print(numeros)
'''


numeros = [[],[] ]
conti = contp = 0
for c in  range(0,7):
    n = int(input('Digite um numero: '))
    if n % 2 == 0:
        if contp == 0 or numeros[0][-1] < n :
            numeros[0].append(n)
        else:
            pos = 0
            while pos < len(numeros[0]):
                if numeros[0][pos] >= n:
                    numeros[0].insert(pos,n)
                    break
                pos += 1
        contp += 1
    else:
        if conti == 0 or numeros[1][-1] < n:
            numeros[1].append(n)
        else:
            pos = 0
            while pos < len(numeros[1]):
                if numeros[1][pos] >= n:
                    numeros[1].insert(pos,n)
                    break
                pos += 1
        conti += 1
print(numeros)


# professor

numeros = [[],[] ]
conti = contp = 0
for c in  range(0,7):
    n = int(input('Digite um numero: '))
    if n % 2 == 0:
        numeros[0].append(n)
    else:
        numeros[1].append(n)
numeros[0].sort()  
numeros[1].sort()    
print(numeros)

