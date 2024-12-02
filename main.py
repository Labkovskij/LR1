import numpy as np
from models import generate_experiment_data
from analysis import calculate_statistics
from visualization import plot_histogram

# Основний блок
if __name__ == "__main__":
    # Параметри моделі
    a, b, c, d = 1, -2, 3, -4  # Параметри кубічної функції
    mu, sigma = 0, 5  # Параметри похибки
    x = np.linspace(-10, 10, 100)  # Інтервал

    # Генерація даних
    data = generate_experiment_data(x, a, b, c, d, mu, sigma)

    # Аналіз даних
    mean, variance, std_dev = calculate_statistics(data)
    print(f"Mean: {mean}, Variance: {variance}, Std Dev: {std_dev}")

    # Візуалізація
    plot_histogram(data, "Histogram of Experimental Data")