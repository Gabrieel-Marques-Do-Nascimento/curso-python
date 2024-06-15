from random import randint

n1 = n2 = n3 = n4 = n5 = 0
for c in range(1,6):
  n = randint(1,10)
  if c == 1:
    n1 = n
  if c == 2:
    n2 = n
  if c == 3:
    n3 = n
  if c == 4:
    n4 = n
  n5 = n
tupla1 = (n1,n2,n3,n4,n5)  
print(f'os valores sorteados foram: {tupla1}')

print(f'O maior valor sorteado foi {max(tupla1)}')
print(f'O menor valor sorteado foi {min(tupla1)}')