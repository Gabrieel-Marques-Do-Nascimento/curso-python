'''
leia a autura de uma parede em metros calcule sua area e a quantidade de tinta necessaria para pintala , cada litro pinta 2m quadrados'''
paredAlt = int(input('diga qual a Autura: '))
paredLarg = int(input('diga qual a Largura: '))
metroQuadrado = paredLarg*paredAlt
print(f'sua parede gastara {metroQuadrado/2} Litros de tinta')
