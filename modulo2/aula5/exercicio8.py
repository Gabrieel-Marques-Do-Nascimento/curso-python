# Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:      APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.
frase = str(input('Digite uma frase: ')).strip().upper()
separa = frase.split()
junta = ''.join(separa)
inversp = ''
print(junta)
for letra in range(len(junta) -1 , -1, -1):
    inversp += junta[letra]
print('O inverso de {} e {}'.format(junta, inversp))
if junta == inversp:
    print('E UM PALINDROMO')
else:
    print('Nao e um palindromo')