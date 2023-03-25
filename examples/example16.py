import numpy as np
import matplotlib.pyplot as plt

def coef_binomial(n, k):
    return np.math.factorial(n) // (np.math.factorial(k) * np.math.factorial(n - k))

def polinomio_bernstein(n, i, t):
    return coef_binomial(n, i) * t**i * (1 - t)**(n - i)

def plot_bernstein(n):
    t = np.linspace(0, 1, 100)
    plt.figure(figsize=(10, 6))

    for i in range(n+1):
        B = polinomio_bernstein(n, i, t)
        plt.plot(t, B, label=f'B_{i},{n}(t)')

    plt.title(f'Polinômios de Bernstein de Grau {n}')
    plt.xlabel('t')
    plt.ylabel('B_i,n(t)')
    plt.legend()
    plt.grid()
    plt.show()

n = 5  # Grau do polinômio de Bernstein
plot_bernstein(n)
