# -*- coding: utf-8 -*-
"""
Created on Sun Nov 16 18:37:28 2025

@author: daynoryamil
"""
# múltiples gráficos mejorados sin seaborn
import matplotlib.pyplot as plt

# Ajustar tamaño general + espacio para título global
fig, ax = plt.subplots(2, 2, figsize=(10, 9), sharey=True)

dias = ['L', 'M', 'X', 'J', 'V', 'S', 'D']
temperaturas = {
    'Cochabamba': [28.5, 30.5, 31, 30, 28, 27.5, 30.5],
    'Santa Cruz': [24.5, 25.5, 26.5, 25, 26.5, 24.5, 25]
}

# Rango común para evitar espacios vacíos
ax[0][0].set_ylim(24, 32)

# --- Gráfico 1 (línea Cochabamba) ---
ax[0, 0].plot(dias, temperaturas['Cochabamba'], color='tab:purple', linewidth=2)
ax[0, 0].set_title("Cochabamba - Línea", fontsize=12, fontweight='bold')
ax[0, 0].set_ylabel("Temperatura (°C)")
ax[0, 0].grid(axis='y', linestyle='--', alpha=0.5)

# --- Gráfico 2 (línea Santa Cruz) ---
ax[0, 1].plot(dias, temperaturas['Santa Cruz'], color='tab:orange', linewidth=2)
ax[0, 1].set_title("Santa Cruz - Línea", fontsize=12, fontweight='bold')
ax[0, 1].set_ylabel("Temperatura (°C)")
ax[0, 1].grid(axis='y', linestyle='--', alpha=0.5)

# --- Gráfico 3 (barras Cochabamba) ---
ax[1, 0].bar(dias, temperaturas['Cochabamba'], color='tab:purple', alpha=0.85)
ax[1, 0].set_title("Cochabamba - Barras", fontsize=12, fontweight='bold')
ax[1, 0].set_xlabel("Días")
ax[1, 0].set_ylabel("Temperatura (°C)")
ax[1, 0].grid(axis='y', linestyle='--', alpha=0.5)

# --- Gráfico 4 (barras Santa Cruz) ---
ax[1, 1].bar(dias, temperaturas['Santa Cruz'], color='tab:orange', alpha=0.85)
ax[1, 1].set_title("Santa Cruz - Barras", fontsize=12, fontweight='bold')
ax[1, 1].set_xlabel("Días")
ax[1, 1].grid(axis='y', linestyle='--', alpha=0.5)

# ================================
# TÍTULO GLOBAL
# ================================
fig.suptitle(
    "Comparación de Temperaturas Semanales\nCochabamba vs Santa Cruz",
    fontsize=18,
    fontweight='bold',
    color='darkblue'
)

plt.tight_layout(rect=[0, 0, 1, 0.95])  # Dejar espacio para el título global
plt.show()
