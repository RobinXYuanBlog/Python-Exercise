import numpy as np
import matplotlib.pyplot as plt

# plt
# x = np.arange(1, 11, 1)
#
# plt.plot(x, x*2, label='Normal')
# plt.plot(x, x*3, label='Fast')
# plt.plot(x, x*4, label='Faster')
#
# plt.legend(loc=0, ncol=3)
#
# plt.show()

# OO
x = np.arange(1, 11, 1)

fig = plt.figure()

ax = fig.add_subplot(111)

l, = plt.plot(x, x)


# plt.legend(['ax legend'])

l.set_label(['ax legend'])

plt.legend()

plt.show()