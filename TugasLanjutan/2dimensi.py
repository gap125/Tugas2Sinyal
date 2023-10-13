# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 21:12:59 2023

@author: ADMIN
"""
print('Nama : Ghazi Amalul Putra')
print('NRP  : 5009211010')

import numpy as np
import matplotlib.pyplot as plt
import cmath

# Buat matriks 2D contoh
image = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12],
                  [13, 14, 15, 16]])

# Ukuran matriks
M, N = image.shape

# FFT 2D manual
fft_result_manual = np.zeros((M, N), dtype=complex)

for u in range(M):
    for v in range(N):
        for x in range(M):
            for y in range(N):
                fft_result_manual[u, v] += image[x, y] * cmath.exp(-2j * cmath.pi * (u * x / M + v * y / N))

# FFT 2D dengan NumPy
fft_result_numpy = np.fft.fft2(image)

# Plot gambar asli
plt.figure(figsize=(12, 4))
plt.subplot(131)
plt.imshow(image, cmap='gray')
plt.title('Gambar Asli')
plt.axis('off')

# Plot hasil FFT manual
plt.subplot(132)
fft_magnitude_manual = np.abs(fft_result_manual)
plt.imshow(np.log(1 + fft_magnitude_manual), cmap='gray')
plt.title('Spektrum Frekuensi (FFT Manual)')
plt.axis('off')

# Plot hasil FFT NumPy
plt.subplot(133)
fft_magnitude_numpy = np.abs(fft_result_numpy)
plt.imshow(np.log(1 + fft_magnitude_numpy), cmap='gray')
plt.title('Spektrum Frekuensi (FFT NumPy)')
plt.axis('off')

plt.tight_layout()
plt.show()
