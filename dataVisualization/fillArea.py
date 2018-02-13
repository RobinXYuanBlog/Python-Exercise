import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 5 * np.pi, 1000)

y1 = np.sin(x)
y2 = np.sin(2*x)

# plt.plot(x, y1)
# plt.plot(x, y2)

# plt.fill(x, y1, 'b', alpha=0.3)
# plt.fill(x, y2, 'r', alpha=0.3)

# plt.plot(x, y1, color='k')
# plt.plot(x, y2, color='r')

plt.fill_between(x, y1, y2, where=y1 >= y2, facecolor='c', alpha=0.3, interpolate=True)
plt.fill_between(x, y1, y2, where=y1 <= y2, facecolor='y', alpha=0.5, interpolate=True)

plt.show()