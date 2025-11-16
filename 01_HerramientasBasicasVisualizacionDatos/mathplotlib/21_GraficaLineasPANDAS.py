# -*- coding: utf-8 -*-
"""
Created on Sun Nov 16 18:41:30 2025

@author: dayno
"""

import pandas as pd
import matplotlib.pyplot as plt

# Datos
df = pd.DataFrame({
    'Dias': ['L', 'M', 'X', 'J', 'V', 'S', 'D'],
    'Cochabamba': [28.5, 30.5, 31, 30, 28, 27.5, 30.5],
    'Santa_cruz': [24.5, 25.5, 26.5, 25, 26.5, 24.5, 25]
})

# Figura
fig, ax = plt.subplots(figsize=(10, 6))

# Graficar líneas
ax.plot(df['Dias'], df['Cochabamba'], 
        color='tab:purple', linewidth=2.5, marker='o', markersize=8,
        label='Cochabamba')

ax.plot(df['Dias'], df['Santa_cruz'], 
        color='tab:green', linewidth=2.5, marker='s', markersize=8,
        label='Santa Cruz')

# ============================
#   ANOTACIONES DE VALORES
# ============================
for d, t in zip(df['Dias'], df['Cochabamba']):
    ax.text(d, t + 0.3, f"{t}", color='tab:purple',
            ha='center', fontsize=12, fontweight='bold')

for d, t in zip(df['Dias'], df['Santa_cruz']):
    ax.text(d, t + 0.3, f"{t}", color='tab:green',
            ha='center', fontsize=12, fontweight='bold')

# ============================
#   ESTÉTICA DEL GRÁFICO
# ============================
ax.set_title("Evolución semanal de la temperatura (°C)",
             fontsize=20, fontweight='bold', color='darkblue')

ax.set_xlabel("Días de la semana", fontsize=14, fontweight='bold')
ax.set_ylabel("Temperatura (°C)", fontsize=14, fontweight='bold')

ax.set_ylim(22, 33)
ax.grid(axis='y', linestyle='--', alpha=0.6)

ax.legend(loc='upper left', frameon=True, shadow=True,
          facecolor='white', edgecolor='gray', fontsize=12)

# ============================
#      FIRMA FINAL
# ============================
fig.text(0.5, -0.02,
         "Elaborado por Daynor Bautista Conde",
         ha='center', fontsize=12, color='gray')

plt.tight_layout()
plt.show()
