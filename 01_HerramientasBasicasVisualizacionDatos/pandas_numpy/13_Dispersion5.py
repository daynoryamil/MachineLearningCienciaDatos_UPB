# -*- coding: utf-8 -*-
"""
Created on Mon Nov 24 22:10:16 2025

@author: dayno
"""

"""
utilización del mapa de colores viridis, Pastel1_r
despliegue del mapa de colores
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colores = np.array([0, 10, 20, 40, 45, 50, 55, 60, 70, 80, 90, 100, 110])  # ← AGREGAMOS UN VALOR

plt.scatter(x, y, c=colores, cmap='Pastel1_r')
plt.colorbar()
plt.show()
