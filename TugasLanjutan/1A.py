# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 01:16:56 2023

@author: ADMIN
"""
print('Nama : Ghazi Amalul Putra')
print('NRP  : 5009211010')

import numpy as np
import cmath
import matplotlib.pyplot as plt

# Tentukan parameter
faktorPengali = 0.5  
panjangInterval = 2 * faktorPengali 
N = 2048  

# Sampling
t = np.linspace(-panjangInterval, panjangInterval, N, endpoint=False) 

# Buat fungsi
def f(t):
    if abs(t) <= faktorPengali:
        return 1.0
    else:
        return 0.0

# FFT Manual
F_manual = [0] * N

for k in range(N):
    Fk = 0
    for j in range(N):
        Fk += f(t[j]) * cmath.exp(-2j * cmath.pi * k * j / N)
    F_manual[k] = Fk

# Validasi NumPy
F_numpy = np.fft.fft([f(tj) for tj in t])

# Hitung spektrum frekuensi
freqs = [k / panjangInterval for k in range(N)]

# Plot sinyal asli
plt.figure(figsize=(10, 6))
plt.subplot(311)
plt.plot(t, [f(tj) for tj in t])
plt.title('Sinyal Asli')
plt.grid()

# Plot hasil manual
plt.subplot(312)
plt.plot(freqs, [abs(Fk) for Fk in F_manual])
plt.title('Spektrum Frekuensi (FFT Manual)')
plt.grid()

# Plot hasil NumPy
plt.subplot(313)
plt.plot(freqs, np.abs(F_numpy))
plt.title('Spektrum Frekuensi (FFT NumPy)')
plt.grid()

plt.tight_layout()
plt.show()
