import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
d = float(input("d: "))

N = int(input("Número de puntos en la dirección x (N): "))
M = int(input("Número de puntos en la dirección y (M): "))
h = (b - a) / N
k = (d - c) / M
w = np.zeros((N+1, M+1))  # Usar NumPy para inicializar la matriz de forma más eficiente

# Condiciones de contorno
for i in range(N+1):
    w[i][0] = 0  # u(x, 0) = 0
    w[i][M] = (a + i * h)**2  # u(x, 1) = x^2

for j in range(M+1):
    w[0][j] = 1 - (c + j * k)**2  # u(0, y) = 1 - y^2
    w[N][j] = 1 - (c + j * k)**2  # u(1, y) = 1 - y^2

# Resolución de la ecuación de Laplace mediante el método de diferencias finitas
for _ in range(100):
    for i in range(1, N):
        for j in range(1, M):
            w[i][j] = 0.25 * (w[i+1][j] + w[i-1][j] + w[i][j+1] + w[i][j-1])

# Crear las coordenadas para el gráfico 3D utilizando np.arange
X = np.arange(a, b+h, h)
Y = np.arange(c, d+k, k)
X, Y = np.meshgrid(X, Y)

# Crear la figura 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Graficar la solución en 3D
ax.plot_surface(X, Y, w, cmap='viridis')

# Configuraciones adicionales del gráfico
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('Solución de la ecuación de Laplace')

# Mostrar el gráfico
plt.show()
