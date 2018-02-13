import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-10, 11, 0.01)

y = x*x

plt.plot(x, y)

plt.annotate('This is the bottom', xy=(0, 0), xytext=(0, 20), arrowprops=dict(facecolor='r', shrink=0.1))

plt.show()