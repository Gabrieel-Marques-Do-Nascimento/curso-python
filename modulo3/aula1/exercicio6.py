tupla = ('Saudade','Cafune','Esperança','Serendipidade','Amor','Luz','Beleza',  'Aurora','Infinito','Poente', 'Chat-gpt')

vogais = 'AEIOU'
print()
cont = frase = 0
for c in range(0,len(tupla)):
  print(f"na palavra {tupla[c]} temos as vogais: ", end='')
  frase = tupla[c]
  for i in range(0,len(frase)):
    if frase[i] in 'Aa':
      print(frase[i],end='')
    if frase[i] in 'Ee':
      print(frase[i],end='')
    if frase[i] in 'Ii':
      print(frase[i],end='')
    if frase[i] in 'Oo':
      print(frase[i],end='')
    if frase[i] in 'Uu':
      print(frase[i],end='')
  print()
  
  # professor
  
  tupla = ('Saudade','Cafune','Esperança','Serendipidade','Amor','Luz','Beleza',  'Aurora','Infinito','Poente', 'Chat-gpt')

vogais = 'AEIOU'
print()
cont = frase = 0
for c in range(0,len(tupla)):
  print(f"na palavra {tupla[c]} temos as vogais: ", end='')
  frase = tupla[c]
  for i in range(0,len(frase)):
    if frase[i] in 'AaUuOoEeIi':
      print(frase[i].lower(),end='')

  print()
    