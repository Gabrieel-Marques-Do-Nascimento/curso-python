'''
Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

– IMC abaixo de 18,5: Abaixo do Peso

– Entre 18,5 e 25: Peso Ideal

– 25 até 30: Sobrepeso

– 30 até 40: Obesidade

– Acima de 40: Obesidade Mórbida
'''
peso = float(input('PESO: (kg) '))
altura = float(input('ALTURA: (m) '))
imc = peso/(altura**2)

print(f' o IMC dessa pessoa e de {imc:.1f}')
if imc < 18.5:
    saude = 'voce esta Abaixo do Peso'
elif imc >= 18.5 and imc < 25:
    saude = 'voce esta com Peso Ideal'
elif imc >= 25 and imc < 30:
    saude = 'voce esta com SobrePeso '
elif imc >= 30 and imc < 40:
    saude = 'voce esta com Obesidade '
else: # elif imc >= 40:
    saude = 'voce esta com Obesidade Morbidade, cuidado '
print(saude)






