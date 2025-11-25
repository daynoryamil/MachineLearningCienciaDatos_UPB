# -*- coding: utf-8 -*-
"""
Created on Mon Nov 24 21:59:44 2025

@author: dayno
"""

# ejemplo con la libreria numpy
# colores, formas
# varias gráficas en uno
import numpy as np
import matplotlib.pyplot as plt

# tiempo muestreado uniformemente a intervalos de 200 ms
t = np.arange(0.0, 5.0, 0.2)

# guiones rojos, cuadrados azules y triángulos verdes
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()
