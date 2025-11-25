# -*- coding: utf-8 -*-
"""
Created on Mon Nov 24 22:03:22 2025

@author: dayno
"""

"""
ejemplos del uso de:
np.arange()
np.random.randint(0, 50, 25)
np.random.randn(25)
"""

import numpy as np
import matplotlib.pyplot as plt

datos = {'a': np.arange(25),
         'b': np.random.randint(0, 50, 25),
         'd': np.random.randn(25)}

datos['b'] = datos['b'] + 10 * np.random.randn(25)
datos['d'] = np.abs(datos['d']) * 100

plt.scatter('a', 'b', c='c', s='d', data=datos)
plt.xlabel('datos de la variable a')
plt.ylabel('datos de la variable b')
plt.show()
