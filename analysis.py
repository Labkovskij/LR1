import numpy as np

# Розрахунок статистичних характеристик
def calculate_statistics(data):
    mean = np.mean(data)
    variance = np.var(data)
    std_dev = np.std(data)
    return mean, variance, std_dev