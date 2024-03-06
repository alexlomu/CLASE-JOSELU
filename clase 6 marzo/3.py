import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Parámetros del dominio y la malla
a, b = 0, np.pi
c, d = 0, 10
N, M = int(input("Número de puntos en la dirección x (N): ")), int(input("Número de puntos en la dirección y (M): "))
h, k = (b - a) / N, (d - c) / M
v = float(input("Valor de velocidad: "))  # 0.5
p = v * k / h

# Inicializar la matriz de solución
w = np.zeros((M + 1, N + 1))

def f(x, b):
    if x < b/2:
        return x
    else:
        return b - x

def g(x):
    return np.sin(x)

# Condiciones de contorno
for i in range(1, N):
    w[0][i] = f(h * i, b)
    w[1][i] = w[0][i] + k * g(h * i)

for j in range(1, M):
    w[j][0] = 0
    w[j][N] = 0

# Método de diferencias finitas
for j in range(1, M):
    for i in range(1, N):
        w[j+1][i] = 2 * (1 - p**2) * w[j][i] - w[j-1][i] + p**2 * (w[j][i+1] + w[j][i-1])

# Crear coordenadas para el gráfico 3D
X = np.linspace(a, b, N+1)
Y = np.linspace(c, d, M+1)
X, Y = np.meshgrid(X, Y)

# Crear gráfico 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Graficar la solución en 3D
ax.plot_surface(X, Y, w, cmap='viridis')

# Configuraciones adicionales del gráfico
ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')
ax.set_zlabel('Eje Z')
ax.set_title('Solución de la ecuación de Helmholtz con condiciones de contorno específicas')

# Mostrar el gráfico
plt.show()
