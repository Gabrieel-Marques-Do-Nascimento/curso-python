


tupla = ('Saudade','Cafune','Esperança','Serendipidade','Amor','Luz','Beleza',  'Aurora','Infinito','Poente', 'Chat-gpt')

vogais = 'AEIOU'
print()
cont = conta = 0
for c in range(0,len(tupla)):
  print(f"na palavra {tupla[c]} temos as vogais: ", end='')
  frase = 'Saudade'
  frasetm = len(frase)
  for i in range(0,6):
    if frase in 'Aa':
            print(f'{vogais[i]}',end=" ")
            #print(tupla[c].count('a'))
            cont = cont + 1
       
  print()
# frase = 'Saudade'
# if frase.upper() in 'Aa':
#     print('oi')
    