num =  cont = 0
sn = ' '
numeross = list()
while True:
    cont = cont+1
    if sn[0] in 'S' or cont == 1:
        num = int(input('Digite um numero: '))
        if num not in numeross:
            print('\033[32mAdicionado com sucesso...\033[m')
            numeross.append(num)
        else:
            print('\033[31mnumero duplicado nao posso adicionar\033[m')
    elif sn[0] in 'N':
        print('fim. ',end='')
        break
    sn = str(input('Quer continuar:[S/N] ')).strip().upper()
    if sn[0] not in 'SN':
        print('\033[31mERRO')
        print('tente novamente.\033[m',end='')
print(23*'\033[1m-=\033[m')
numeross.sort()
print(f'os valores digitados foram {numeross}')



    