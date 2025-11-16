# -*- coding: utf-8 -*-
"""
Created on Sun Nov 16 18:33:19 2025

@author: dayno
"""

import matplotlib.pyplot as plt
plt.style.use('seaborn-v0_8')

fig, ax = plt.subplots(figsize=(10, 6))

dias = ['L', 'M', 'X', 'J', 'V', 'S', 'D']
temperaturas = {
    'Cochabamba': [28.5, 30.5, 31, 30, 28, 27.5, 30.5],
    'Santa Cruz': [24.5, 25.5, 26.5, 25, 26.5, 24.5, 25]
}

# Líneas con marcadores
ax.plot(
    dias, temperaturas['Cochabamba'], 
    label='Cochabamba',
    color='tab:purple', linewidth=2.5,
    marker='o', markersize=8
)

ax.plot(
    dias, temperaturas['Santa Cruz'], 
    label='Santa Cruz',
    color='tab:green', linewidth=2.5,
    marker='s', markersize=8
)

# ============================
#  ETIQUETAS DE LOS VALORES
# ============================

# Para Cochabamba
for d, t in zip(dias, temperaturas['Cochabamba']):
    ax.text(d, t + 0.3, f"{t}",
            color='tab:purple', fontsize=12,
            ha='center', fontweight='bold')

# Para Santa Cruz
for d, t in zip(dias, temperaturas['Santa Cruz']):
    ax.text(d, t + 0.3, f"{t}",
            color='tab:green', fontsize=12,
            ha='center', fontweight='bold')

# Título de la gráfica
ax.set_title(
    "Evolución semanal de la temperatura (°C)",
    fontsize=20, fontweight='bold', color='darkblue'
)

# Etiquetas de ejes
ax.set_xlabel("Días de la semana", fontsize=14, fontweight='bold')
ax.set_ylabel("Temperatura (°C)", fontsize=14, fontweight='bold')

# Rango eje Y
ax.set_ylim(20, 35)

# Grid profesional
ax.grid(axis='y', color='gray', linestyle='--', linewidth=0.8, alpha=0.7)

# Leyenda
ax.legend(
    fontsize=12, loc='upper right',
    frameon=True, shadow=True,
    facecolor='white', edgecolor='gray'
)

# ============================
#      FIRMA FINAL
# ============================

fig.text(
    0.5, -0.02, 
    "Elaborado por Daynor Bautista Conde",
    ha='center', fontsize=12, color='gray'
)

plt.tight_layout()
plt.show()
