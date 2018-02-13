import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10, 11, 1)

plt.plot(x, x*x)

# plt.axis([-5, 5, 0, 10])

# plt.xlim([-5, 5])

plt.ylim([0, 60])

plt.show()