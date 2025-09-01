import numpy as np
import matplotlib.pyplot as plt

# Definição da função
def f(x):
    return np.exp(-x**2)

# Intervalo de integração
a, b = 0, 2

# Número de subdivisões
n = 10
dx = (b - a) / n

# Pontos de partição
x = np.linspace(a, b, n+1)

# Somas de Riemann
left_sum = np.sum(f(x[:-1]) * dx)       # Esquerda
right_sum = np.sum(f(x[1:]) * dx)       # Direita
midpoints = a + (np.arange(n) + 0.5) * dx
mid_sum = np.sum(f(midpoints) * dx)     # Ponto médio

print("Soma de Riemann (esquerda):", left_sum)
print("Soma de Riemann (direita):", right_sum)
print("Soma de Riemann (ponto médio):", mid_sum)

# Gráfico com os retângulos da soma à esquerda
X = np.linspace(a, b, 400)
Y = f(X)

plt.plot(X, Y, 'r-', linewidth=2, label="f(x) = e^(-x²)")

for xi in x[:-1]:
    plt.bar(xi, f(xi), width=dx, alpha=0.3, align="edge", edgecolor="k")

plt.xlabel("x")
plt.ylabel("f(x)")
plt.title(f"Soma de Riemann à esquerda (n = {n})")
plt.legend()
plt.show()
