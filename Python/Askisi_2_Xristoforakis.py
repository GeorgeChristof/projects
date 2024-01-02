import fft_modules
from fft_modules import *
import numpy as np
from numpy import pi, sin, linspace, abs, cos, arange, array, ones
import matplotlib.pyplot as plt
from scipy import fftpack, arange
from scipy.fftpack import fft, fftshift


plirof = [0, 1, 0, 1, 1, 0, 1, 0, 1] #πληροφορια
num_of_bits = 8 #arithmos twn bit
data_rate = 500 
Ac = 1  #platos feron simatos
Fc = 2000 #suxnothta feron simatos
t_met = num_of_bits / data_rate #xronos metadoshs ths plhroforias
Tc = 1/Fc #periodos carrier
t_bit = 1/data_rate #xronos gia 1 bit plhroforias
F_nyquist = 2*Fc
T_nyquist = 1/Fc
F_sample = 10*F_nyquist
T_sample = 1/F_sample
 
xAxis = np.arange(0, len(plirof))
yAxis = np.array(plirof)
plt.step(xAxis,yAxis)
plt.figure(1)
plt.title('Πληροφορία')
plt.xlabel('Χρόνος (sec) ->')
plt.ylabel ('Πλάτος (V) ->')
plt.show() #σχήμα που απεικονίζει την πληροφορία για την διάρκεια του χρόνου μετάδοσης της

plt.figure(2)
plt.subplot(1,2,1)
Tmax = t_met
t= linspace(0, Tmax, int(Tmax/T_sample))  #πίνακας χρόνου
total_samples = len(t)
carrier = Ac * sin(2 * pi * Fc * t)
frequencies, amfipleyro=fft_modules.amfipleyro_fasma(carrier, t)
plt.stem(frequencies,amfipleyro)
plt.xlim(-4*Fc,4*Fc)
plt.title('Αμφίπλευρο φάσμα πληροφορίας')
plt.xlabel('Συχνότητα (Hz) ->')
plt.ylabel ('Πλάτος')
plt.grid('on')

plt.subplot(1,2,2)
frequencies, monopleyro=fft_modules.monopleyro_fasma(carrier,t)
plt.stem(frequencies,monopleyro)
plt.xlim(0, 4*Fc)
plt.title('Μονόπλευρο φάσμα πληροφορίας')
plt.xlabel('Συχνότητα (Hz) ->')
plt.ylabel ('Πλάτος') 
plt.grid('on')

plt.figure(3)
plt.subplot(1,2,1)
frequencies, amfipleyro=fft_modules.amfipleyro_fasma(carrier, t)
plt.plot(frequencies,amfipleyro)
plt.xlim(-4*Fc,4*Fc)
plt.title('Αμφίπλευρο φάσμα φέρον')
plt.xlabel('Συχνότητα (Hz) ->')
plt.ylabel ('Πλάτος')
plt.grid('on')

plt.subplot(1,2,2)
frequencies, monopleyro=fft_modules.monopleyro_fasma(carrier,t)
plt.plot(frequencies,monopleyro)
plt.xlim(0, 4*Fc)
plt.title('Μονόπλευρο φάσμα φέρον')
plt.xlabel('Συχνότητα (Hz) ->')
plt.ylabel ('Πλάτος') 
plt.grid('on')

ASK_sign = np.ones(num_of_bits)
for i in range (0, num_of_bits):
    if plirof[i] == 0:
        ASK_sign[i] = 0
    elif plirof == 1:
        ASK_sign[i] = carrier[i]

plt.figure(4)
#plt.plot(t,ASK_sign)
plt.title('ASK σήμα')
plt.xlabel('Χρόνος σε sec')
plt.ylabel('Πλάτος σε V')
plt.grid('on')

plt.figure(5)
frequencies, amfipleyro = fft_modules.amfipleyro_fasma(ASK_sign, t)
plt.plot(frequencies,amfipleyro)
plt.title('Αμφίπλευρο φάσμα ASK σήματος')
plt.xlabel('Συχνότητα (Hz)')
plt.ylabel('Πλάτος (V)')
plt.grid('on')