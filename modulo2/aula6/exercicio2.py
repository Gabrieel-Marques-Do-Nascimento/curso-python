# Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

# print("""Sou o seu Computador....
# Acabei de pensar em um numero entre 0 e 10.
# Sera que voce consegue adivinhar qual foi? """)
# aleatorio = randint(1,10)
# num = 0
# cont = 0
# while num != aleatorio:
#     cont = cont + 1
#     num = int(input('Qual o seu palpite?? '))
#     if num < aleatorio:
#         print('MAIS... tente mais uma vez')
#     elif num > aleatorio:
#         print('MENOS... tente mais uma vez')
# print('Acertou com {} tentativas. **PARABENS**'.format(cont))


# professor

print("""Sou o seu Computador....
Acabei de pensar em um numero entre 0 e 10.
Sera que voce consegue adivinhar qual foi? """)
computador = randint(1,10)
acertou = False
palpites = 0
while not acertou :
    palpites = palpites + 1
    jogador = int(input('Qual o seu palpite?? '))
    if jogador == computador:
        acertou= True
    else:
        if jogador < computador:
             print('MAIS... tente mais uma vez')
        elif jogador > computador:
            print('MENOS... tente mais uma vez')
print('Acertou com {} tentativas. **PARABENS**'.format(palpites))
