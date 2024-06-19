# # notas [ ['gabriel', [ 18,19]]]  no final um boletim com media
# lista = []
# #  lista = [['gabriel', [44,55]], ['joao', [55,66]] ]
# while True:
#   aluno = str(input('Nome do aluno: '))
#   alunos = [[int(input('Nota 1:')),int(input('Nota 2:'))]]
#   alunos.insert(0,aluno) # type: ignore
#   lista.append(alunos[:])
#   alunos.clear()
#   contn = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
#   if contn in 'N':
#     break
# print(30*'-=')
# print('No.   NOME         MEDIA')
# print(26*'-')
# for c in range(0,len(lista)):
#   media = ( lista[c][1][0] + lista[c][1][1]) /2 #len(lista[c][1])
#   print(f'{c:<5} {lista[c][0]:15} {media:>}')
# print(26*'-')
# while True:
#   contar = int(input('Mostrar nota de qual Aluno? [999 interronper]: '))
#   if contar != 999:
#     print(f'Notas de {lista[contar][0]} são {lista[contar][1]}')
#   elif contar == 999:
#     break
# print('FINALIZANDO...')
# print('<<< VOLTE SEMPRE >>>')

# PROFESSOR

alunos = []

while True:
  nome = str(input('Nome do aluno: '))
  nota1 = float(input('Nota 1:'))
  nota2 = float(input('Nota 2:'))

  media = (nota1 + nota2) / 2
  alunos.append([nome , [nota1 , nota2] ,media])
  contn = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
  if contn in 'N':
    break
print(30*'-=')
print(f'{"No.":<4}   {"NOME":<10}  {"MEDIA":>8}')
print(26*'-')
for i, a in enumerate(alunos):
    print(f'{i:<4}   {a[0]:<10}  {a[2]:>8.1f}')
while True:
  contar = int(input('Mostrar nota de qual Aluno? [999 interronper]: '))
  if contar <= len(alunos)-1:
    print(f'Notas de {alunos[contar][0]} são {alunos[contar][1]}')
  elif contar == 999:
    break
print('FINALIZANDO...')
print('<<< VOLTE SEMPRE >>>')
print('FINALIZANDO...')
print('<<< VOLTE SEMPRE >>>')