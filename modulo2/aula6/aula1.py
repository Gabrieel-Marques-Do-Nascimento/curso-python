# Nessa aula, vamos continuar a estudar os laços e vamos aprender a usar a estrutura de repetição while no Python. Por exemplo:

# c=1 while c !=10:

# print(c)

# c+=1

# print(‘Acabou’)









# r = 'S'
# soma = 0
# while r == 'S':
#     n = int(input('digite um numero: '))
#     r = str(input('Quer continuar [S/N]: ')).upper()
#     soma = soma + n
# print(' A soma dos valores e {}'.format(soma))

# mostrar se o numero e impar ou par digitando 0 termina  mas o 0 e uma essecao 0 deve ser nulo

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um numero: '))
    if n != 0:
        if n % 2 == 0:
             par = par + 1
        else:
            impar = impar + 1
print('Voce digitou {} numeros pares e {} numeros impares'.format(par , impar))



