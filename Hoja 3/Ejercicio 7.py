import kbhit
import numpy as np
import portaudio as pr
import pyaudio as py


p = py.PyAudio()
CHUNK = 1024
SRATE = 44100


stream = p.open(
	format=py.paFloat32,
	channels=1,
	rate=SRATE,
	output=True
)

def osc(fre,dur,vol):
	return (vol*np.sin(2*np.pi*np.arange(int(SRATE*dur))*fre/SRATE))

def frecNotas(nota, dur):
	global fre
	a = len(nota)

	if nota[:1] == 'G' or nota[:1] == 'g':
		fre = 783.991
	elif nota[:1] == 'A' or nota[:1] == 'a':
		fre = 880
	elif nota[:1] == 'C' or nota[:1] == 'c':
		fre = 523.251
	elif nota[:1] == 'B' or nota[:1] == 'b':
		fre = 987.767
	elif nota[:1] == 'F' or nota[:1] == 'f':
		fre = 698.456
	elif nota[:1] == 'E' or nota[:1] == 'e':
		fre = 659.255
	elif nota[:1] == 'D' or nota[:1] == 'd':
		fre = 587.33
	elif nota[:1] == '&':
		fre = 0

		
	if a > 1:
		if nota[-1] == '>':
			fre = fre*np.power(2,(a-1))
		else:
			fre = fre/np.power(2,(a-1))


	block = osc(fre,dur,1)
	stream.write(block.astype(np.float32).tobytes())


hbd = [('G',0.5),('&',0.0001),('G',0.5),('A',1.0),('G',1.0),('c>',1.0),('B',2.0),('G',0.5),('&',0.0001),('G',0.5),('A',1.0),('G',1.0),('d>',1.0),('c>',2.0),('G',0.5),('&',0.0001),('G',0.5),('g>',1.0),('e>',1.0),('c>',1.0),('B',1.0),('A',1.0),('f>',0.5),('&',0.0001),('f>',0.5),('e>',1.0),('c>',1.0),('d>',1.0),('c>',2.0)]

for tupla in hbd:
	frecNotas(tupla[0],tupla[1])


	