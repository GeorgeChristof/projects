# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 00:42:20 2021

@author: okg13
"""

import numpy as np
from numpy import pi,sin,linspace,abs,cos
import matplotlib.pyplot as plt
from scipy import fftpack,arange
from scipy.fftpack import fft,fftshift

A = 4 #platos
f = 10 #syxnothta
Fnyq = 2*f #elaxisth syxnothta deigmatolipsias
T = 1/f #periodos
tmax = 5*T #synolikh xronikh diarkeia symatos
Ts = T/1000 #xronos deigmatoleipsias = periodos / arithmos deigmatwn ana periodo
Fs = 1/Ts #syxnothta deigmatolipsias

t = linspace(0,tmax, int(tmax/Ts)) #pinakas xronou
total_samples = len(t) #synolikos arithmos deigmatwn

my_signal = A*cos(2*pi*f*t) #to sunhmitoniko shma

#sxediash tou shmatos
plt.figure(1)
plt.plot(t, my_signal)
plt.xlabel('χρόνος (seconds) ->')
plt.ylabel('Πλάτος ->')
plt.title('Το συνημιτονικό σήμα')
plt.grid('on')

#xrhsh ths fft synartishs
plt.figure(2)
fft_my_signal = fft(my_signal)
norm_fft_my_signal = abs(fft_my_signal) / total_samples

#sxediash platous me xrhsh abs
plt.plot(norm_fft_my_signal)
plt.xlabel('Αύξων αριθμός δείγματος ->')
plt.ylabel('Πλάτος ->')
plt.title('Επίδραση της συνάρτησης fft με κανονικοποιηση Πλ')
plt.grid('on')

#αμφιπλευρο φασμα
if total_samples%2==0:
    k=linspace(-total_samples/2,total_samples/2-1,total_samples)            # Ο αριθμός των δειγμάτων είναι άρτιος
else:
    k=linspace(-(total_samples-1)/2,(total_samples-1)/2,total_samples)      # Ο αριθμός των δειγμάτων είναι περιττός
    
Duration=total_samples*Ts
frequency_Range=k*(1/Duration) #αξονας των συχνοτητων
final_fft = fftshift(norm_fft_my_signal) #κεντραρισμα φασματικων συνιστωσων στις σωστες συχνοτητες

#σχεδιαση του αμφιπλευρου φασματος
plt.figure(3)
plt.subplot(2,1,1)
plt.plot(frequency_Range,final_fft)
plt.xlim(-50,50)
plt.ylim(0,2*A)
plt.xlabel('Συχνότητα (Hz) ->')
plt.ylabel('Πλάτος ->')
plt.title('Αμφίπλευρο φάσμα')
plt.grid('on')

monopleyro = final_fft*2
plt.subplot(2,1,2)
plt.plot(frequency_Range,monopleyro)
plt.xlim(0,50)
plt.ylim(0,2*A)
plt.xlabel('Συχνότητα (Hz) ->')
plt.ylabel('Πλάτος ->')
plt.title('Μονοπλευρο')
plt.grid('on')

#ενεργειακη φασματικη πυκνοτητα
A = A**2
plt.figure(4)
plt.subplot(2,1,1)
plt.plot(frequency_Range,final_fft)
plt.xlim(0,50)
plt.ylim(0,A**2+4)
plt.xlabel('Συχνότητα (Hz) ->')
plt.ylabel('Πλάτος ->')
plt.title('Ενεργειακή φασματική πυκνότητα')
plt.grid('on')

plt.subplot(2,1,2)
plt.plot(frequency_Range,monopleyro)
plt.xlim(0,50)
plt.ylim(0,A**2+4)
plt.xlabel('Συχνότητα (Hz) ->')
plt.ylabel('Πλάτος ->')
plt.grid('on')