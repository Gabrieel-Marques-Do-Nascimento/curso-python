'''
Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

– Média abaixo de 5.0: REPROVADO

– Média entre 5.0 e 6.9: RECUPERAÇÃO

– Média 7.0 ou superior: APROVADO
'''
pprova = float(input('primeira nota: '))
sprova = float(input('Segunda nota: '))
media = (pprova+sprova)/2
print(f'Tirando {pprova} e {sprova}, a media do aluno e {media:.1f}')

if media < 5.0:
    print('aluno esta REPROVADO')
elif media >= 5.0 < 6.9: # 
    print('aluno esta EM RECUPERACAO')
elif media >= 7.0:
    print('aluno esta APROVADO')
    
    # PROFESSOR
    
    
#  USANDO IF COM ELIF NAO FUNCIONA ISSO =  6.9 < media >= 5.0 
if  6.9 < media >= 5.0 : #  IF media >= 5.0 and media < 6.9: 
    print('aluno esta EM RECUPERACAO')
elif media < 5.0:
    print('aluno esta REPROVADO')    
elif media >= 7.0:
    print('aluno esta APROVADO')