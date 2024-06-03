'''
Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
'''
# normalmente
km = float(input('Qual distacia da sua viagem: '))

print(f'vc esta prestes a comecar uma viagem de {km:.1f}Km.')

if km <= 200:
    print(f'E o preco da sua passagem sera de {km*0.50:.2f}R$')
else:
    print(f'E o preco da sua passagem sera de {km*0.45:.2f}R$')

# SIMPLIFICADO
presso = km*0.50 if km <= 200 else km * 0.45
print(f'E o preco da sua passagem sera de {presso:.2f}R$') 

