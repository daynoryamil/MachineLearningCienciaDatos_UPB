# -*- coding: utf-8 -*-
"""
Created on Sun Nov 16 18:27:05 2025

@author: dayno
"""

import matplotlib.pyplot as plt

fig, ax = plt.subplots()
dias = ['L', 'M', 'X', 'J', 'V', 'S', 'D']
temperaturas = {
    'Cochabamba': [28.5, 30.5, 31, 30, 28, 27.5, 30.5],
    'Santa Cruz': [24.5, 25.5, 26.5, 25, 26.5, 24.5, 25]
}

# cambia el estilo de líneas
ax.plot(dias, temperaturas['Cochabamba'], linestyle='dashed')
ax.plot(dias, temperaturas['Santa Cruz'], linestyle='dotted')

# combinación de marcadores y colores
"""
ax.plot(dias, temperaturas['Cochabamba'], 
        color='tab:purple', marker='^', linestyle='dashed')
ax.plot(dias, temperaturas['Santa Cruz'], 
        color='tab:green', marker='o', linestyle='dotted')
"""

plt.show()
