import numpy as np
import matplotlib.pyplot as plt

# plt method
# y = np.arange(1, 5)
# plt.plot(y, y*2)
# plt.grid(True, color='r', linewidth='0.5', linestyle='--')
# plt.show()

# OO method
x = np.arange(0, 10, 1)
fig = plt.figure()

ax = fig.add_subplot()

plt.plot(x, x*2)

plt.grid(color='r', linestyle='-.', linewidth='0.5')

plt.show()