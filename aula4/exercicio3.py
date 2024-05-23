'''
A média (Me) é calculada somando-se todos os valores de um conjunto de dados e dividindo-se pelo número de elementos deste conjunto.

programa q leia duas notas e calcule a media'''

portugues1 = int(input('digite sua nota da prova1 '))
portugues2 = int(input('digite sua nota da prova2 '))
exempl = 0
media = [portugues1 , portugues2 ]
print(f'sua media em portugues foi : {(portugues1+portugues2 )/len(media)}')  
'''  len()  === pega quantidade de item do arry ex: media = [portugues1 , portugues2 ] === 2      '''