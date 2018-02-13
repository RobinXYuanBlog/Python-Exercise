import numpy as np
import matplotlib.pyplot as plt

# height = [161, 170, 182, 175, 173, 165]
# weight = [50, 58, 80, 70, 69, 55]
#
# plt.scatter(height, weight)
#
# plt.show()

N = 1000

x = np.random.randn(N)
y1 = np.random.randn(N)

y = x + np.random.randn(N)

#plt.scatter(x, y)
# plt.show()

# Scatter

plt.scatter(x, y, s=10, c='red', alpha=0.5)
plt.show()