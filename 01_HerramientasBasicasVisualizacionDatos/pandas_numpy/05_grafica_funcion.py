# -*- coding: utf-8 -*-
"""
Created on Mon Nov 24 21:58:43 2025

@author: dayno
"""

from numpy import linspace, sin, pi
import matplotlib.pyplot as plt

x = linspace(-pi, pi, 200)
y = sin(x**2 + 1)

plt.plot(x, y)
plt.show()
