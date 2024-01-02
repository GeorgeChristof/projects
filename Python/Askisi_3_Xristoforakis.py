
import fft_modules
from fft_modules import *
import numpy as np
from numpy import pi, sin, linspace, abs, cos
import matplotlib.pyplot as plt
from scipy import fftpack, arange
from scipy.fftpack import fft, fftshift

leksi = [1,0,1,1,0,1,0,1]
data_rate = 500
bit_duration = 1/500 #xronos gia 1 bit plhroforias
number_of_bits = len(leksi)
bits_time = bit_duration*number_of_bits #xronos gia na metadothei h plhroforia

Ac = 1 #platos ferontos
Fc = 2000 #syxnothta ferontos
Fdev = 500 #apoklish syxnothtas ##### thn allazw gia to erwthma 5 Fdev = 1000
Fc_high = Fc + Fdev #upshlh syxnothta
Fc_low = Fc - Fdev #xamhlh syxnothta
F_nyquist = 2*Fc 
Fsamp = 10*F_nyquist #syxnothta deigmatolhpsias
Tc = 1/Fc #periodos ferontos
Tsamp = 1/Fsamp
samp_bit = bit_duration/Tsamp #arithmos deigmatwn gia 1 bit
Tmax = bits_time

t= linspace(0,Tmax,int(Tmax/Tsamp))
carrier = Ac*sin(2*pi*Fc*t)

carrier_high = Ac*sin(2*pi*Fc_high*t)
carrier_low = Ac*sin(2*pi*Fc_low*t)

plt.figure(1)
plt.subplot(3,1,1)
plt.plot(t,carrier)
plt.title("Φέρον Σήμα")
plt.xlabel("Χρόνος σε sec")
plt.ylabel("Πλάτος σε V")
plt.xlim(0,bit_duration)

plt.subplot(3,1,2)
plt.plot(t,carrier_high)
plt.title("Φέρον υψηλής συχνότητας")
plt.xlabel("Χρόνος σε sec")
plt.ylabel("Πλάτος σε V")
plt.xlim(0,bit_duration)

plt.subplot(3,1,3)
plt.plot(t,carrier_low)
plt.title("Φέρον χαμηλής συχνότητας")
plt.xlabel("Χρόνος σε sec")
plt.ylabel("Πλάτος σε V")
plt.xlim(0,bit_duration)
plt.show()

plt.figure(2)
plt.subplot(3,1,1)
frequencies, amfipleyro=fft_modules.amfipleyro_fasma(carrier,t)
plt.plot(frequencies, amfipleyro)
plt.title("Αμφίπλευρο φάσμα φέροντος")
plt.xlabel("Συχνότητα σε Hz")
plt.ylabel("Πλάτος σε V")

plt.subplot(3,1,2)
frequencies, amfipleyro=fft_modules.amfipleyro_fasma(carrier_high,t)
plt.plot(frequencies, amfipleyro)
plt.title("Αμφίπλευρο φάσμα υψηλής συχνότητας")
plt.xlabel("Συχνότητα σε Hz")
plt.ylabel("Πλάτος σε V")

plt.subplot(3,1,3)
frequencies, amfipleyro=fft_modules.amfipleyro_fasma(carrier_low,t)
plt.plot(frequencies, amfipleyro)
plt.title("Αμφίπλευρο φάσμα χαμηλής συχνότητας")
plt.xlabel("Συχνότητα σε Hz")
plt.ylabel("Πλάτος σε V")
plt.show()

plt.figure(3)
plt.subplot(3,1,1)
frequencies, monopleyro=fft_modules.monopleyro_fasma(carrier,t)
plt.plot(frequencies, monopleyro)
plt.title("Μονόπλευρο φάσμα φέροντος")
plt.xlabel("Συχνότητα σε Hz")
plt.ylabel("Πλάτος σε V")

plt.subplot(3,1,2)
frequencies, monopleyro=fft_modules.monopleyro_fasma(carrier_high,t)
plt.plot(frequencies, monopleyro)
plt.title("Μονόπλευρο φάσμα υψηλής συχνότητας")
plt.xlabel("Συχνότητα σε Hz")
plt.ylabel("Πλάτος σε V")

plt.subplot(3,1,3)
frequencies, monopleyro=fft_modules.monopleyro_fasma(carrier_low,t)
plt.plot(frequencies,monopleyro)
plt.title("Μονόπλευρο φάσμα χαμηλής συχνότητας")
plt.xlabel("Συχνότητα σε Hz")
plt.ylabel("Πλάτος σε V")
plt.show()

pliroforia = []
for i in range (0,len(leksi)):
    pin = np.ones(int(samp_bit))
    x=pin*leksi[i]
    pliroforia=np.concatenate((pliroforia,x))
    
plt.figure(4)
plt.plot(t,pliroforia)
plt.title("Το σήμα πληροφορίας")
plt.xlabel("Χρόνος σε sec")
plt.ylabel("Πλάτος σε V")
plt.show()

FSKsign = np.ones(len(pliroforia))
for i in range (0,len(pliroforia)):
    if pliroforia[i] == 0:
        FSKsign[i] = carrier_low[i]
    elif pliroforia[i] == 1:
        FSKsign[i] = carrier_high[i]
        
plt.figure(5)
plt.plot(t,FSKsign)
plt.title("FSK σήμα")
plt.xlabel("Χρόνος σε sec")
plt.ylabel("Πλάτος σε V")
plt.show()

plt.figure(6)
plt.subplot(2,1,1)
frequencies, amfipleyro=fft_modules.amfipleyro_fasma(FSKsign,t)
plt.plot(frequencies, amfipleyro)
plt.title("Αμφίπλευρο φάσμα FSK σήματος")
plt.xlabel("Συχνότητα σε Hz")
plt.ylabel("Πλάτος σε V")

plt.subplot(2,1,2)
frequencies, monopleyro=fft_modules.monopleyro_fasma(FSKsign,t)
plt.plot(frequencies, monopleyro)
plt.title("Μονόπλευρο φάσμα FSK σήματος")
plt.xlabel("Συχνότητα σε Hz")
plt.ylabel("Πλάτος σε V")
plt.show()

#Fdev = 1000
plt.figure(7)
frequencies, monopleyro=fft_modules.monopleyro_fasma(FSKsign,t)
plt.plot(frequencies, monopleyro)
plt.title("Μονόπλευρο φάσμα FSK σήματος με fdev = 1kHz")
plt.xlabel("Συχνότητα σε Hz")
plt.ylabel("Πλάτος σε V")
plt.show()