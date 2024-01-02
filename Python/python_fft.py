# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 23:55:29 2018

@author: admin
"""
import numpy as np
from numpy import pi, sin, linspace, abs, cos
import matplotlib.pyplot as plt
from scipy import fftpack, arange
from scipy.fftpack import fft, fftshift

A=5
f=1000                              #συχνότητα
T=1/f                               #περίοδος
Nyquist_Freq=2*f                    #ελάχιστη συχνότητα δειγματοληψίας (Nyquist frequency)
number_of_signal_periods=3          #αριθμός περιόδων του σήματος
Tmax=number_of_signal_periods*T     #Συνολική χρονική διάρκεια του σήματος
samples_per_period=100              #αριθμός δειγμάτων ανά περίοδο
Ts=T/samples_per_period             #Χρόνος δειγματοληψίας
Fs = 1/Ts                           #συχνότητα δειγματοληψίας (=samples_per_period*f)

t= linspace(0, Tmax, int(Tmax/Ts))  #πίνακας χρόνου
total_samples = len(t)              #συνολικός αριθμός δειγμάτων που θα ληφθούν κατά την διάρκεια του σήματος
 
my_signal = A*sin(2*pi*f*t) #+10*sin(2000*2*pi*t) +cos(2*pi*3000*t)    #Το ημιτονικό σήμα
 
#Σχεδίαση του ημιτονικού σήματος στο πεδίο του χρόνου

plt.figure(1)
plt.plot(t,my_signal)
plt.xlabel('χρόνος (seconds) ->')
plt.ylabel('Πλάτος ->')
plt.title('Το ημιτονικό σήμα')
plt.grid('on')

 
# Χρήση της fft (scipy.fftpack.fft) για τον υπολογισμό του Ταχύ Μετασχηματισμού Fourier (Fast Fourier Transform - FFT) του σήματος

plt.figure(2)
FFT_of_my_signal = fft(my_signal)   #επίδραση της fft στο my_signal)

# Σχεδίαση του πλάτους (με χρήση της abs) του σήματος στο οποίο έχει επιδράσει η fft συνάρτηση
plt.plot(abs(FFT_of_my_signal))    
plt.xlabel('Αύξων αριθμός δείγματος ->')
plt.ylabel('Πλάτος ->')
plt.title('Επίδραση της συνάρτησης fft')
plt.grid('on')

# Σημαντικές παρατηρήσεις:
# 1: Το πλάτος είναι ίσο με το πλάτος του σήματος επί το μισό του συνολικού αριθμού των δειγμάτων (Α*total_samples/2)
# 2: Ο οριζόντιος άξονας είναι βαθμονομημένος σε αύξοντα αριθμό δειγμάτων
# 3: Οι φασματικές συνιστώσες δεν είναι κεντραρισμένες σωστά

# Τα παραπάνω πρέπει να διορθωθούν για να πάρουμε τον κανονικό μετασχηματισμό fourier του σήματος, δηλαδή:
# Ο άξονας του πλάτους θα πρέπει να κανονικοποιηθεί σε σχέση με τον συνολικό αριθμό των δειγμάτων, 
# Ο οριζόντιος άξονας θα πρέπει να αντικατασταθεί με συχνότητες, και οι συχνότητες πρέπει να κεντραριστούν σωστά


# Στα παρακάτω θα δημιουργήσουμε αμφίπλευρο φάσμα πλάτους

# Βήμα πρώτο: Κανονικοποίηση του κατακόρυφου άξονα (άξονας πλάτους)
# Λύση: απλά διαιρούμε το πλάτος του σήματος (στο οποίο έχει επιδράσει η fft) με:
#      το μισό του συνολικού αριθμού των δειγμάτων όταν πρόκειται για μονόπλευρο φάσμα,ή
#      τον συνολικό αριθμό των δειγμάτων όταν πρόκειται για αμφίπλευρο φάσμα

Normalized_FFT_of_my_signal=abs(FFT_of_my_signal)/total_samples              #διαιρούμε με τον συνολικό αριθμό των δειγμάτων
plt.figure(3)
plt.plot(Normalized_FFT_of_my_signal)
plt.xlabel('Αύξων αριθμός δείγματος ->')
plt.ylabel('Πλάτος ->')
plt.title('Κανονικοποίηση ως πρός το πλάτος')
plt.grid('on')

# Βήμα δεύτερο: Δημιουργούμε τον άξονα των συχνοτήτων. 
# Λαμβάνουμε υπόψιν τον συνολικό αριθμό δειγμάτων αν είναι άρτιος ή περιττός, και
# Δημιουργούμε και θετικές και αρνητικές συχνότητες για να δούμε το αμφίπλευρο φάσμα του σήματος
# Δημιουργούμε τον πίνακα (άξονα) των συχνοτήτων από -Fs/2 ως Fs/2 


if total_samples%2==0:
    k=linspace(-total_samples/2,total_samples/2-1,total_samples)            # Ο αριθμός των δειγμάτων είναι άρτιος
else:
    k=linspace(-(total_samples-1)/2,(total_samples-1)/2,total_samples)      # Ο αριθμός των δειγμάτων είναι περιττός

Duration=total_samples*Ts 
frequency_Range=k*(1/Duration)                                              # O  άξονας των συχνοτήτων

# Σχεδίαση του ακεντράριστου φάσματος
plt.figure(4)
plt.plot(frequency_Range,Normalized_FFT_of_my_signal)
plt.xlabel('Συχνότητα (Hz) ->')
plt.ylabel('Πλάτος ->')
plt.title('Ακεντράριστο αμφίπλευρο φάσμα με άξονα συχνοτήτων από -Fs/2 ως Fs/2')

# Βήμα τρίτο: Κεντράρουμε τις φασματικές συνιστώσς σωστά (στις συχνότητες -f και +f, όπου f είναι η συχνότητα του σήματος
# Αυτό γίνεται με την συνάρτηση fftshift (scipy.fftpack.fftshift)

Final_fft=fftshift(Normalized_FFT_of_my_signal)                             #κεντράρισμα των φασματικών συνιστωσών στις σωστές συχνότητες

# Σχεδίαση του τελικού αμφίπλευρου φάσματος
plt.figure(5)
plt.plot(frequency_Range,Final_fft)
plt.xlabel('Συχνότητα (Hz) ->')
plt.ylabel('Πλάτος ->')
plt.title('Κεντραρισμένο αμίπλευρο φάσμα από -Fs/2 ως Fs/2')
plt.grid('on')

# Αλλαγή κλίμακας οριζόντιου άξονα και stem διάγραμμα
# Aν θέλετε δοκιμάστε τις παρακάτω εντολές
plt.figure(6)
plt.plot(frequency_Range,Final_fft)
plt.axis([-5000,5000,-2,5])
plt.yticks(arange(-1,5,0.5))
plt.xticks(arange(-5000,5000,1000))
plt.title('Κεντραρισμένο αμίπλευρο φάσμα από -5000 ως 5000')
plt.grid('on')

plt.figure(7)
plt.stem(frequency_Range,Final_fft)
plt.axis([-5000,5000,-2,5])
plt.yticks(arange(-1,5,0.5))
plt.xticks(arange(-5000,5000,1000))
plt.title('Κεντραρισμένο αμίπλευρο φάσμα από -5000 ως 5000')
plt.grid('on')
