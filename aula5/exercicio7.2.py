# importar a biblioteca pygame
from pygame import mixer,event

# uma forma de implementar o código
mixer.init()

# substitua o nome do arquivo "musica.mp3" pelo seu arquivo mp3
mixer.music.load('musicas\Bleach • Edit Mangá _ After Dark(MP3_320K).mp3')
mixer.music.play()
x = input('Digite algo para parar...')