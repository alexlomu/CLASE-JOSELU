import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parámetros
L = 1.0  # Longitud de la barra
T = 1.0  # Tiempo total
nx = 6  # Número de puntos de la malla espacial
nt = 4  # Número de pasos de tiempo
alpha = 0.01  # Coeficiente de difusión térmica

dx = L / (nx - 1)
dt = T / nt

# Crear malla espacial
x = np.linspace(0, L, nx)
t = np.linspace(0, T, nt)

# Inicializar la temperatura
u = np.zeros((nt, nx))
u[0, int(nx/2)] = 1.0  # Fuente de calor en el medio de la barra en el tiempo 0

# Iteración temporal (Diferencias finitas explícitas)
for n in range(1, nt):
    for i in range(1, nx - 1):
        u[n, i] = u[n-1, i] + alpha * dt / dx**2 * (u[n-1, i+1] - 2*u[n-1, i] + u[n-1, i-1])

# Crear malla para la gráfica en 3D
X, T = np.meshgrid(x, t)

# Visualización de la temperatura en 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, T, u, cmap='viridis')
ax.set_title('Distribución de temperatura en la barra')
ax.set_xlabel('Posición')
ax.set_ylabel('Tiempo')
ax.set_zlabel('Temperatura')
plt.show()
