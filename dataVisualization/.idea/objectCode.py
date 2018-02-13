from pylab import *
import matplotlib.pylab as plt
import numpy as np

# pylab
# x = arange(0, 10, 1)
# y = randn(len(x))
#
# plot(x, y)
#
# title('pylab')

# pyplot
# x = np.arange(0, 10, 1)
# y = np.random.randn(len(x))
#
# plt.plot(x, y)
# plt.title('pyplot')

# object
x = np.arange(0, 10, 1)
y = np.random.randn(len(x))

fig = plt.figure()

ax = fig.add_subplot(111)

l, = plt.plot(x, y)

show()