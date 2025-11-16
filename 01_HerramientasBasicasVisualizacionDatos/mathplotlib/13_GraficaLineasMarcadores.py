# -*- coding: utf-8 -*-
"""
Created on Sun Nov 16 18:24:07 2025

@author: dayno
"""

import matplotlib.pyplot as plt

fig, ax = plt.subplots()
dias = ['L', 'M', 'X', 'J', 'V', 'S', 'D']
temperaturas = {
    'Cochabamba': [28.5, 30.5, 31, 30, 28, 27.5, 30.5],
    'Santa Cruz': [24.5, 25.5, 26.5, 25, 26.5, 24.5, 25]
}

# cambio de color
# ax.plot(dias, temperaturas['Cochabamba'], color='tab:purple')
# ax.plot(dias, temperaturas['Santa Cruz'], color='tab:green')

# cambio de marcadores
# ax.plot(dias, temperaturas['Cochabamba'], marker='^^')
# ax.plot(dias, temperaturas['Santa Cruz'], marker='o')

# combinación de marcadores y colores
ax.plot(dias, temperaturas['Cochabamba'], color='tab:purple', marker='^')
ax.plot(dias, temperaturas['Santa Cruz'], color='tab:green', marker='o')

plt.show()
