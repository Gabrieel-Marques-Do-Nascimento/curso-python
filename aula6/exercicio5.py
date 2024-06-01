'''
Exercício Python 26: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
'''
frase = str(input('Digite uma frase: ')).upper().strip()
qntd= frase.count('A')
posit = frase.find('A')
ult_posit = frase.rfind('A')
print(f'A letra "A" apareceu {qntd} vezes na frase')
print(f'A letra "A" apareceu primeiro na posicao {posit+1}')
print(f'A ultima letra "A" apareceu na posicao {ult_posit+1} ')



