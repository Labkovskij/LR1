import numpy as np

# Генерація похибки (нормальний розподіл)
def generate_error(mu, sigma, size):
    return np.random.normal(mu, sigma, size)

# Кубічна функція
def cubic_function(x, a, b, c, d):
    return a * x**3 + b * x**2 + c * x + d

# Генерація експериментальних даних
def generate_experiment_data(x, a, b, c, d, mu, sigma):
    process = cubic_function(x, a, b, c, d)
    error = generate_error(mu, sigma, len(x))
    return process + error