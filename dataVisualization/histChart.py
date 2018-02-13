import numpy as np
import matplotlib.pyplot as plt

# ms = 100
# sigma = 20
# x = ms + sigma * np.random.randn(20000)
#
# plt.hist(x, bins=100, color='blue', normed=False)
# plt.show()

# Double Variables
x = np.random.randn(1000) + 2
y = np.random.randn(1000) + 3

plt.hist2d(x, y, bins=40)
plt.show()