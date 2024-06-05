'''
Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''
import datetime
ano = datetime.date.today().year
data = int(input('data de nascimento: '))
sexo = int(input('sexo: \n[ 1 ]masculino\n[ 2 ]feminino\n ESCOLHA: '))
idade = ano-data 
print(f'quem nasceu em {data} tem {ano-data} Anos em {ano}')

if sexo == 1:
    if idade < 18:
        print(f'falta {18-idade} Anos para o seu ALISTAMENTO')
        print(f'Seu alistamento sera em {ano+(18-idade)}')
    elif idade == 18:
        print(f'Corre chegou a hora de se ALISTAR')
    elif idade > 18:
        print(f'voce ja deveria ter se ALISTADO ha {idade-18} Anos')
        print(f'seu alistamento foi em {data+18}')
elif sexo == 2:
    print('Alistamento nao. OBRIGATORIO!')