# -*- coding: utf-8 -*-
"""
Created on Mon Nov 24 22:11:34 2025

@author: dayno
"""

"""
graficas con variables categóricas
"""

import matplotlib.pyplot as plt

categorias = ['grupo_a', 'grupo_b', 'grupo_c']
valores = [1, 10, 100]

plt.figure(figsize=(9, 3))

plt.subplot(131)
plt.bar(categorias, valores)

plt.subplot(132)
plt.scatter(categorias, valores)

plt.subplot(133)
plt.plot(categorias, valores)

plt.suptitle('trazado de variables categóricas')
plt.show()
