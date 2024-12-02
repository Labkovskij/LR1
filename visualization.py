import matplotlib.pyplot as plt

# Побудова гістограми
def plot_histogram(data, title):
    plt.hist(data, bins=30, alpha=0.7, color='blue')
    plt.title(title)
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.grid()
    plt.show()