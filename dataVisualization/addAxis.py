import numpy as np
import matplotlib.pyplot as plt

# pyplot


y = np.arange(2, 20, 1)
x1 = y*y
x2 = np.log(y)

plt.plot(y, x1)

plt.twiny()

plt.plot(y, x2, 'r')

plt.show()
