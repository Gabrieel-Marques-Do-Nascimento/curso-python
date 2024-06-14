# Qual valor voce quer sacar?  
# Total de {:2.2f} cedulas de R$50  
# Total de {:2.2f}cedulas de R$20
# Total de {:2.2f} cedulas de R$10
# Total de {:2.2f} cedulas de R$1
# Volte sempre ao Banco DN! Tenha um bom dia.


# cinquenta = 50
# vinte = 20
# des = 10
# um = 1
# resto = 0
# print(30*'=')
# print('          \033[32mBANCO GN\033[m')
# print(30*'=')
# dim = int(input('Qual valor voce quer sacar? R$'))
# saldo =5000
# if dim <= saldo:
#     while dim /50 >= 1:
#         cinquenta = dim // cinquenta
#         print(f'Total de {cinquenta:2.0f} cedulas de R$50')
#         break
#     resto = dim -  (cinquenta*50)

#     while resto/vinte >= 1:
#         vinte = resto//vinte
#         print(f'Total de {vinte:2.0f} cedulas de R$20') 
#         break
#     resto = resto - (vinte*20)

#     while resto/des >=1:
#         des = resto//des
#         print(f'Total de {des:2.0f} cedulas de R$10')
#         break
#     resto = resto - (des*10)
#     while resto/ um  >= 1:
#         um = resto//um
#         print(f'Total de {um:2.0f} cedulas de R$1')
#         break
# else:
#     print('\033[31mSaldo insuficiente\033[m')


# professor

dim = int(input('Qual valor voce quer sacar? R$'))
total = dim 
cedula = 50
ncedulas = 0
while True:
    if total >= cedula:
        total-= cedula
        ncedulas += 1
    else:
        if ncedulas > 0:
             print(f'Total de {ncedulas:2.0f} cedulas de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        ncedulas = 0
        if total == 0 :
            break