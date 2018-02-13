import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-10, 11, 1)
y = x*x

plt.plot(x, y)

plt.text(-5, 40, 'function: y=x^2', family='serif', size=20, color='w', style='italic',
         weight='black', bbox=dict(facecolor='gray', alpha=0.5))

plt.show()