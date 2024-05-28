# import math  # v1 importa todas bibliotecas
from math import sqrt,floor
num = int(input('digite um numero'))
# rais = math.sqrt(num)  #v1 tem q referenciar meth 
rais = sqrt(num)  # nao precisa referenciar por quer foi importado sqrt
print(f'a rais quadrada de {num} e {rais:.2}')