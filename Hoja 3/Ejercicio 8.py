import kbhit as kb
import pyaudio as py
import wave
import numpy as np


wf = wave.open('piano.wav', 'rb')
p = py.PyAudio()

CHUNK = 1024
SRATE = 44100

tecla= ' '


data = wf.readframes(wf.getnframes())

#def osc(fre,dur,vol):
 # return (vol*np.sin(2*np.pi*np.arange(int(SRATE*dur))*fre/SRATE))

def escala():
    tecla = kb.KBHit().getch()
    frec = wf.getframerate()
    ok = False
    i = 0
    if tecla=='z':
        ok = True
    elif tecla =='x':
        ok = True
        frec = frec*np.power(2,float(2/12))
    elif tecla == 'c':
        ok = True
        while i < 2:
            frec = frec*np.power(2,float(2/12))
            i = i+1
    elif tecla == 'v':
        ok = True
        while i < 2:
            frec = frec*np.power(2,float(2/12))
            i = i+1
        frec = frec*np.power(2,float(1/12))
    elif tecla == 'b':
        ok = True
        while i < 3:
            frec = frec*np.power(2,float(2/12))
            i = i+1
        frec = frec*np.power(2,float(1/12))
    elif tecla == 'n':
        ok = True
        while i < 3:
            frec = frec*np.power(2,float(2/12))
            i = i+1
        frec = frec*np.power(2,float(1/12))
        frec = frec*np.power(2,float(2/12))
    elif tecla == 'm':
        ok = True
        while i < 3:
            frec = frec*np.power(2,float(2/12))
            i = i+1
        frec = frec*np.power(2,float(1/12))
        i=0
        while i < 2:
            frec = frec*np.power(2,float(2/12))
            i = i+1

    if ok:
        stream = p.open(
            format=p.get_format_from_width(wf.getsampwidth()),
            channels=wf.getnchannels(),
            rate= int(frec),
            output=True
        )
        stream.write(data)
    else:
        if tecla != 'q':
            print("Las teclas son: z.x.c.v.b.n.m")

print("Las teclas son: z.x.c.v.b.n.m")
while tecla!='q':
    escala()
