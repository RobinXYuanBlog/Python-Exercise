import matplotlib.pyplot as plt
import numpy as np

N = 1000

x = np.random.randn(N)
y = np.random.randn(N)
colors = np.random.rand(N)
area = np.pi * (15 * np.random.rand(N)**2)  # 0 - 15 point radius

plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.show()