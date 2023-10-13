# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 00:05:25 2023

@author: ADMIN
"""
print('Nama : Ghazi Amalul Putra')
print('NRP  : 5009211010')

import numpy as np
import matplotlib.pyplot as plt

def fft(x):
    N = len(x)
    if N <= 1:
        return x
    even = fft(x[0::2])
    odd = fft(x[1::2])
    twiddle_factors = [np.exp(-2j * np.pi * k / N) * odd_k for k, odd_k in enumerate(odd)]
    return [even_k + twiddle_k for even_k, twiddle_k in zip(even, twiddle_factors)] + \
           [even_k - twiddle_k for even_k, twiddle_k in zip(even, twiddle_factors)]

def ifft(x):
    N = len(x)
    if N <= 1:
        return x
    even = ifft(x[0::2])
    odd = ifft(x[1::2])
    twiddle_factors = [np.exp(2j * np.pi * k / N) * odd_k for k, odd_k in enumerate(odd)]
    return [even_k + twiddle_k for even_k, twiddle_k in zip(even, twiddle_factors)] + \
           [even_k - twiddle_k for even_k, twiddle_k in zip(even, twiddle_factors)]

def fft2d(matrix):
    rows, cols = len(matrix), len(matrix[0])

    for i in range(rows):
        matrix[i] = fft(matrix[i])

    for j in range(cols):
        col = [matrix[i][j] for i in range(rows)]
        col = fft(col)
        for i in range(rows):
            matrix[i][j] = col[i]

    return matrix

def MFCC(matrix):
    # Melakukan FFT
    fft_matrix = fft2d(matrix)

    # Melakukan Log dari Spektrogram
    log_spectrum = np.log(np.abs(fft_matrix) ** 2 + 1e-10)

    # Melakukan IFFT
    cepstrum = ifft2d(log_spectrum)

    return cepstrum

def ifft2d(matrix):
    rows, cols = len(matrix), len(matrix[0])

    for i in range(rows):
        matrix[i] = ifft(matrix[i])

    for j in range(cols):
        col = [matrix[i][j] for i in range(rows)]
        col = ifft(col)
        for i in range(rows):
            matrix[i][j] = col[i]

    return matrix

def tampilkan_matrix(matrix, title):
    plt.imshow(np.abs(matrix), cmap='viridis')
    plt.colorbar()
    plt.title(title)
    plt.show()

# Contoh penggunaan dengan matriks input yang berbeda
matriks_input = [
    [0, 1, 2, 3],
    [4, 5, 6, 7],
    [8, 9, 10, 11],
    [12, 13, 14, 15]
]

# Mengubah matriks input
for i in range(len(matriks_input)):
    for j in range(len(matriks_input[0])):
        matriks_input[i][j] += i + j  # Mengubah nilai-nilai matriks

hasil_MFCC= MFCC(matriks_input)

# Menampilkan matriks input yang telah diubah
tampilkan_matrix(matriks_input, 'Matriks Input yang Diubah')

# Menampilkan hasil implementasi MFCC
tampilkan_matrix(hasil_MFCC, 'Implementasi MFCC')