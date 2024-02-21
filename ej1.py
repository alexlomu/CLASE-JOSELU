import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

a = float(input("a "))
b = float(input("b "))
c = float(input("c "))
d = float(input("d "))
N = int(input("N "))
M = int(input("M "))
h = (b - a) / N
k = (d - c) / M
w = np.zeros((N, M))

def f(i, j):
    return 0

for i in range(1, N):
    w[i][0] = 0
    w[i][M-1] = (a + i * h) ** 2
for j in range(1, M):
    w[0][j] = 0
    w[N-1][j] = (b + j * k) ** 2
    
for _ in range(100):
    for i in range(1, N-1):
        for j in range(1, M-1):
            w[i][j] = (k ** 2 * (w[i+1][j] + w[i-1][j]) + h ** 2 * (w[i][j+1] + w[i][j-1]) - (h * k) ** 2 * f(i, j)) / (2 * (h ** 2 + k ** 2))

# Crear mallas para la superficie tridimensional
x = np.linspace(a, b, N)
y = np.linspace(c, d, M)
X, Y = np.meshgrid(x, y)

# Graficar la superficie tridimensional
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, w, cmap='viridis')

# Configurar etiquetas
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()
