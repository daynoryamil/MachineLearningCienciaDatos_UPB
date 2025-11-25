# -*- coding: utf-8 -*-
"""
Created on Mon Nov 24 22:04:30 2025

@author: dayno
"""

"""
ejemplo con uso de colores (hotpink) y RGB
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y, color='hotpink')

x = np.array([2,2,8,1,5,12,3,7,1,14,7,14,12])
y = np.array([100,85,84,105,99,90,95,94,100,79,112,91,90,85])
plt.scatter(x, y, color='#88c999')

plt.show()
