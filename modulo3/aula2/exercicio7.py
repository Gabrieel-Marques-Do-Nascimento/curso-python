# lista =[]
# n = str(input('Digite a esprecao: '))
# lista.append(n)
# cont = aspa1 = aspa2 = aspas =  0
# for item in lista:
#     for esprecao in item:
#         if esprecao in '(':
#             aspa1 = aspa1 + 1
#         elif esprecao in ')':
#             aspa2 = aspa2 + 1
#         aspas= aspa1 + aspa2
#     if aspas % 2 == 0:
#             print('\033[32msua esprecao esta correta\033[m')
#     else:
#             print('\033[31mSua esprecao esta errada!\033[m')


# professor


n = str(input('Digite a esprecao: '))
pilha =[]
for simbl in n:
    if simbl == '(':
        pilha.append('(')
    elif simbl == ')':
        if len(pilha) > 0:
          pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
        print('\033[32msua esprecao esta correta\033[m')
else:
        print('\033[31mSua esprecao esta errada!\033[m')
