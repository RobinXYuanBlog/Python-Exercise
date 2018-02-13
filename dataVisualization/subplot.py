import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 100)

fig = plt.figure()

ax1 = fig.add_subplot(221)
ax1.plot(x, x)

ax2 = fig.add_subplot(222)
ax2.plot(x, -x)

ax3 = fig.add_subplot(223)
ax3.plot(x, x*x)

ax4 = fig.add_subplot(224)
ax4.plot(x, np.log(x))

plt.show()

