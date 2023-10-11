# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 11:24:31 2023

@author: Ghazi
"""

print('Nama : Ghazi Amalul Putra')
print('NRP  : 5009211010')

# Buat fungsi yang mengkonvolusi dua sinyal 1-dimensi
def convolutionSatuDimensi(signal1, signal2):
    len1 = len(signal1)
    len2 = len(signal2)
    result_len = len1 + len2 - 1
    result = [0] * result_len
    
    for i in range(result_len):
        result[i] = 0
        for j in range(len1):
            if i - j >= 0 and i - j < len2:
                result[i] += signal1[j] * signal2[i - j]
    return result

# Input nilai sinyal
signal1 = [10, 20, 30, 40]
signal2 = [0.5, 0.25, 0.25, 0.35]

# Tampilkan hasil convolusi
convolution_result = convolutionSatuDimensi(signal1, signal2)
print("Hasil konvolusi:", convolution_result)

# Validasi hasil dengan Numpy
import numpy as np

numpy_result = np.convolve(signal1, signal2, mode='full')
print("Hasil konvolusi NumPy:", numpy_result)
