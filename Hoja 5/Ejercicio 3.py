#Ana Álava Papí


import pygame 
from pygame.locals import *
import numpy as np
import portaudio as pr
import pyaudio as py


CHUNK = 1024
SRATE = 44100

WIDTH = 64
HEIGHT = 480

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Theremin")
pos_x = 0
pos_y = 0
q = True
frame = 0

p = py.PyAudio()

stream = p.open(
	format=py.paFloat32,
	channels=2,
	rate=SRATE,
	output=True
)

# [(fc,vol),(fm1,beta1),(fm2,beta2),...]
def oscFM(frecs,frame):
    chunk = np.arange(CHUNK)+frame # array de frames
    samples = np.zeros(CHUNK)+frame # acumulador de síntesis

    # recorremos en orden inverso
    for i in range(len(frecs)-1,-1,-1):
        # utilizamos samples como moduladora de una nueva portadora
        samples = frecs[i][1] * np.sin(2*np.pi*frecs[i][0]*chunk/SRATE + samples)

    return samples



while q:
	# obtencion de la posicion del raton 
	for event in pygame.event.get():
		if event.type == pygame.MOUSEMOTION:
			pos_x, pos_y = event.pos
		elif event.type == QUIT:
			q = False
			#pygame.sys.exit()


	posiciones = []

	posiciones.append(pos_x*100)
	posiciones.append(pos_y)

	frecs = []
	frecs.append(posiciones)

	block = oscFM(frecs,frame)
	stream.write(block)

pygame.quit()