# Nessa aula, vamos aprender como utilizar a instrução break e os loopings infinitos a favor das nossas estratégias de código. É muito importante saber usar o break no Python, já que em alguns casos precisamos interromper um laço no meio do caminho.

# Além disso, vamos aprender como trabalhar com as novas fstrings do Python.

soma = n = 0
while True:
    n = int(input('digite um numero: ')) 
    if n == 999:
        break
    soma += n
print(f'A soma dos numeros e {soma}')
    