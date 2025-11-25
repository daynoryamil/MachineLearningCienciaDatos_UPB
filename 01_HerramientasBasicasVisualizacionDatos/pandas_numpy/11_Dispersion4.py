# -*- coding: utf-8 -*-
"""
Created on Mon Nov 24 22:05:38 2025

@author: dayno
"""

"""
utilización de una lista definida de colores
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

mis_colores = np.array(['red', 'green', 'blue', 'yellow', 'pink',
                        'black', 'orange', 'purple', 'beige',
                        'brown', 'gray', 'cyan', 'magenta'])

plt.scatter(x, y, c=mis_colores)
plt.show()
