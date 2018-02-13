import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# x = np.linspace(-10, 10, 10)
# y = x**2

data = pd.read_csv('000001.csv', delimiter=',',
                                header=0, usecols=(0, 1, 4), nrows=500)


plt.plot_date(data['Date'], data['Open'], linestyle='-', color='red', marker='.')
plt.plot_date(data['Date'], data['Close'], linestyle='--', color='blue', marker='.')

plt.show()