import numpy as np
from numpy import pi, sin, linspace, abs, cos
import matplotlib.pyplot as plt
from scipy import fftpack, arange
from scipy.fftpack import fft, fftshift

A1=2
A2=4
A3=8
A = 8
f1 = 100                            #συχνότητα
f2 = 500
f3 = 1000
f = 1000
T=1/f1                               #περίοδος
Nyquist_Freq=3*f1                    #ελάχιστη συχνότητα δειγματοληψίας (Nyquist frequency)
number_of_signal_periods=3          #αριθμός περιόδων του σήματος
Tmax=number_of_signal_periods*T     #Συνολική χρονική διάρκεια του σήματος
Ts = 10*Nyquist_Freq                #Χρόνος δειγματοληψίας
Fs = 1/Ts                           #συχνότητα δειγματοληψίας (=samples_per_period*f)

t = linspace(0, Tmax)               #πίνακας χρόνου #int(Tmax/Ts)
total_samples = len(t)              #συνολικός αριθμός δειγμάτων που θα ληφθούν κατά την διάρκεια του σήματος

signal_1 = A1*cos(2*pi*f1*t)
signal_2 = A2*cos(2*pi*f2*t)
signal_3 = A3*sin(2*pi*f3*t)

##my_signal = A1*cos(2*pi*f1*t) + A2*cos(2*pi*f2*t) + A3*sin(2*pi*f3*t)    #Το σήμα
my_signal = signal_1 + signal_2 + signal_3
#Σχεδίαση του σήματος στο πεδίο του χρόνου

plt.figure(1)
plt.subplot(4,1,1)
plt.plot(t,signal_1)
plt.title('Το σήμα 1,2,3 και το συνθετο')
plt.grid('on')

plt.subplot(4,1,2)
plt.plot(t,signal_2)
plt.xlabel('χρόνος (seconds) ->')
plt.ylabel('Πλάτος ->')
plt.grid('on')

plt.subplot(4,1,3)
plt.plot(t,signal_3)
plt.grid('on')

plt.subplot(4,1,4)
plt.plot(t,my_signal)
plt.xlabel('χρόνος (seconds) ->')
plt.grid('on')

max_f = 2*max(f1,f2,f3)
my_signal = fft(my_signal)
my_signal = fftshift(abs(my_signal))

if total_samples%2==0:
    k=linspace(-total_samples/2,total_samples/2-1,total_samples)            # Ο αριθμός των δειγμάτων είναι άρτιος
else:
    k=linspace(-(total_samples-1)/2,(total_samples-1)/2,total_samples)      # Ο αριθμός των δειγμάτων είναι περιττός
Duration=total_samples*Ts
frequency_Range=k*(1/Duration) #αξονας των συχνοτητων

#σχεδιαση του αμφιπλευρου φασματος
plt.figure(2)
plt.plot(frequency_Range,my_signal)
plt.xlim(-max_f,max_f)
plt.ylim(0,10)
plt.xlabel('Συχνότητα (Hz) ->')
plt.ylabel('Πλάτος ->')
plt.title('Αμφίπλευρο φάσμα')
plt.grid('on')

#σχεδιαση του μονοπλευρου φασματος
mon_signal = 2*my_signal
plt.figure(3)
plt.plot(frequency_Range,my_signal)
plt.xlim(0,max_f)
plt.ylim(0,10)
plt.xlabel('Συχνότητα (Hz) ->')
plt.ylabel('Πλάτος ->')
plt.title('Μονοπλευρο φάσμα')
plt.grid('on')

#ενεργειακη φασματικη πυκνοτητα
A_en = A**2
plt.figure(4)
plt.plot(frequency_Range,my_signal)
plt.xlim(-max_f,max_f)
plt.ylim(0,(2*max(A1,A2,A3)**2 + 6))
plt.xlabel('Συχνότητα (Hz) ->')
plt.ylabel('Πλάτος ->')
plt.title('Ενεργειακή φασματική πυκνότητα')
plt.grid('on')