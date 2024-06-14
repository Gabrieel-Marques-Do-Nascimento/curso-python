pessoas = homen = mulher = 0
while True:
    print('\033[m',25*'-')
    print('   CADASTRE UMA PESSOA')
    print(25*'-')
    idade = int(input('IDADE: \033[35m'))
    sexo = ' '
    while sexo not in 'MmFf':  
         sexo = str(input('\033[mSEXO: [M/F] \033[31m')).strip().upper()[0] 
    print('\033[m',25*'-')
    if idade >= 18:
        pessoas+=1
    if sexo in 'Ff' and idade < 20:
        mulher+=1
    if sexo in 'Mm':
        homen+=1
    contna = ' '
    while contna not in 'SsNn' :
        contna = str(input('\033[mQUER CONTINUAR? [S/N] \033[31m')).strip().upper()[0]
    if contna in 'Nn':
        break
print('\033[m\n========FIM DO PROGRAMA========')
print(f'Total de pessoas com mais de 18 anos: {pessoas} ')
print(f'Ao todo temos {homen} homens cadastrados')
print(f'E temos {mulher} Mulheres com menos de 20 Anos')
'''
print(25*'-')
print('   CADASTRE UMA PESSOA')
print(25*'-')
idade = int(input('IDADE: '))
sexo = str(input('SEXO: [M/F] '))
print(25*'-')
contn = str(input('QUER CONTINUAR? [S/N] '))
print('========FIM DO PROGRAMA========')
print('Tpotal de pessoas com mais de 18 anoe: {} ')
print('Ao todo temos {} homens cadastrados')
print('E temos {} Mulheres com menos de 20 Anos')
'''


# professor