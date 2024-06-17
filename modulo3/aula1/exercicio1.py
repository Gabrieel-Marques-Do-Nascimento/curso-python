# 0 - zero
#1 - um
#2 - dois
#3 - três
#4 - quatro
#5 - cinco
#6 - seis
#7 - sete
#8 - oito
#9 - nove
#10 - dez
#11 - onze
#12 - doze
#13 - treze
#14 - quatorze ou catorze
#15 - quinze
#16 - dezesseis
#17 - dezessete
#18 - dezoito
#19 - dezenove
#20 - vinte
numeros_extenço = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis',
                   'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
                   'quatorze', 'quinze', 'dezesseis', 'dezessete', 'desoito',
                   'dezenove', 'vinte', 'trinta', 'quarenta', 'cinquenta',
                   'sessenta', 'setenta', 'oiitenta', 'noventa', 'cem')
# while True:
#     n = int(input('Digite um número entre 0 e 20: '))
#     while True:
#         if n < 0 or n > 20:
#             n = int(input('Tente novamente. Digite um número entre 0 e 20: '))
#         else:
#             break
#     print(f'Você digitou o número {numeros_extenço[n]}')


# professor



while True:
    n = int(input('Digite um número entre 0 e 20: '))
    if 0 <= n <= 20:
        break
    print('Tente novamente. ',end='')
    
        
print(f'Você digitou o número {numeros_extenço[n]}')

