# -*- coding: utf-8 -*-
"""
Created on Sun Nov 16 18:30:33 2025

@author: dayno
"""

import matplotlib.pyplot as plt

fig, ax = plt.subplots()
dias = ['L', 'M', 'X', 'J', 'V', 'S', 'D']
temperaturas = {
    'Cochabamba': [28.5, 30.5, 31, 30, 28, 27.5, 30.5],
    'Santa Cruz': [24.5, 25.5, 26.5, 25, 26.5, 24.5, 25]
}

ax.plot(dias, temperaturas['Cochabamba'])
ax.plot(dias, temperaturas['Santa Cruz'])

ax.set_xlabel("Días", fontdict={'fontsize': 14, 'fontweight': 'bold', 'color': 'tab:blue'})
ax.set_ylabel("Temperatura ºC")

ax.set_ylim([20, 35])
ax.set_yticks(range(20, 35))

plt.show()
