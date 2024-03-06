import matplotlib.pyplot as plt
import numpy as np

# Parámetros del dominio y la malla
a, b = 0, 10
N = int(input("Número de puntos en la dirección x (N): "))
h = (b - a) / N

# Inicializar la matriz de solución
w = np.zeros(N + 1)
# Definir la condición inicial
w[N//2] = 1

# Método de diferencias finitas para onda no estacionaria
for n in range(1, N):
    w[n] = w[n-1]

# Graficar la solución
plt.plot(np.linspace(a, b, N+1), w)
plt.xlabel('x')
plt.ylabel('Amplitud de la onda')
plt.title('Onda no estacionaria')
plt.grid(True)
plt.show()
