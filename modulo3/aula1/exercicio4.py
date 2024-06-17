# n1 = int(input('digite um numero: '))
# n2= int(input('digite outro numero: '))
# n3 = int(input('digite mais um numero: '))
# n4 = int(input('digite o ultimo numero: '))
# tupla =  (n1,n2,n3,n4)

# print(f'Voce digitou os valores: {tupla}')
# print(f'O valor 9 foi digitado: {tupla.count(9)} vezes')

# if 3  in tupla:
#     print(f'o valor 3 foi digitado na: {tupla.index(3)+1}ᵃ posicao')
# else:
#      print(f'o valor 3 foi digitado em: nenhuma posicao')
# print('Os valores pares digitados foram: ',end='')
# for c in range(0,4):
#     if tupla[c] % 2 == 0:
#         print(tupla[c],end=' ')
# print()        
# professor
contn = ' '
while contn not in 'Nn':
    tupla =  (int(input('digite um numero: ')),int(input('digite outro numero: ')),int(input('digite mais um numero: ')),int(input('digite o ultimo numero: ')))  #

    print(f'Voce digitou os valores: {tupla}')
    print(f'O valor 9 foi digitado: {tupla.count(9)} vezes')

    if 3  in tupla:
        print(f'o valor 3 foi digitado na: {tupla.index(3)+1}ᵃ posicao')
    else:
        print(f'o valor 3 foi digitado em: nenhuma posicao')
    print('Os valores pares digitados foram: ',end='')
    for c in range(0,4):
        if tupla[c] % 2 == 0:
            print(tupla[c],end=' ')
    contn = str(input('\nQuer continuar: [S/N] '))