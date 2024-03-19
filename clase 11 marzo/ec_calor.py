import numpy as np
import matplotlib.pyplot as plt

# Parámetros
L = 1.0  # Longitud de la barra
T = 1.0  # Tiempo total
nx = 100  # Número de puntos de la malla espacial
nt = 1000  # Número de pasos de tiempo
alpha = 0.01  # Coeficiente de difusión térmica

dx = L / (nx - 1)
dt = T / nt

# Crear malla espacial
x = np.linspace(0, L, nx)

# Inicializar la temperatura
u = np.zeros(nx)
u[int(nx/2)] = 1.0  # Fuente de calor en el medio de la barra

# Iteración temporal (Diferencias finitas explícitas)
for n in range(nt):
    un = u.copy()
    for i in range(1, nx - 1):
        u[i] = un[i] + alpha * dt / dx**2 * (un[i+1] - 2*un[i] + un[i-1])

# Visualización de la temperatura
plt.plot(x, u)
plt.title('Distribución de temperatura en la barra')
plt.xlabel('Posición')
plt.ylabel('Temperatura')
plt.grid(True)
plt.show()
