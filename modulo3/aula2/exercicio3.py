# Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
pos = 0
lista = []
for c in range(0,5):
    n = int(input('Digitte um numero: '))
    if c == 0 or n >= lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista')
    else:
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos,n)
                print(f'Adicionado na posicao {pos}')
                break
            pos += 1
print(f'Os valores digitados em ordem: {lista}')    