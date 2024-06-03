'''Exercício Python 18: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.  '''
import math
angulo = float(input('digite um angulo: '))
seno = math.sin(math.radians(angulo)) #  radians = converte para graus
coseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print(f'o seno e {seno:.3f} do angulo de  {angulo:.3f} \no coseno e {coseno:.3f} do angulo de  {angulo:.3f} \na tangente e {tangente:.3f} do angulo de  {angulo:.3f}')


