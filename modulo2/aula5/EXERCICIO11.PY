#Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
'''
media = 0
idoso = 0
idosoidade = 0
mulhermenor20 = 0
cont = 0
homen = 0
mulher = 0
for pessoas in range(1,5):
    print(10*'=',end='')
    print(f' {pessoas}ᵃ PESSOA ', end='') 
    print(10*'=')
    nome = str(input('NOME: '))
    idade = float(input('IDADE: '))
    sexo = str(input('SEXO [M/F]: '))
    media += idade
    if pessoas == 1 :
        idoso = nome
        idosoidade = idade
    else:
        if idade > idosoidade and sexo == 'm':
           
            idoso = nome
            idosoidade = idade
    if idade < 20 and sexo == 'f':
     
        cont = cont + 1
print(f'A media de idade do grupo e {media/4}')

print(f'O homen mais velho tem {idosoidade} anos e se chama {idoso}')

print('AO TODO SÃO {} MULHERES MENORES QUE 20 ANOS'.format(cont))
'''

# professor

media = 0
nomevelho = 0
maioridadeHomen = 0
somaIdade = 0
mediaidade = 0
totmulhermenor = 0
for pessoas in range(1,5):
    print(f'---------- {pessoas}ᵃ PESSOA ----------') 
    nome = str(input('NOME: ')).strip()
    idade = float(input('IDADE: '))
    sexo = str(input('SEXO [M/F]: '))
    somaIdade += idade
    if pessoas == 1 and sexo in 'Mm':
        maioridadeHomen = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadeHomen:
         maioridadeHomen = idade
         nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulhermenor += 1
mediaidade = somaIdade / 4
print(f'A media de idade do grupo e {mediaidade}')

print(f'O homen mais velho tem {maioridadeHomen} anos e se chama {nomevelho}')

print('AO TODO SÃO {} MULHERES MENORES QUE 20 ANOS'.format(totmulhermenor))