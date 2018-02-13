import numpy as np
import matplotlib.pyplot as plt

np.random.seed(100)

# data = np.random.normal(size=1000, loc=0, scale=1)

# plt.boxplot(data, sym='.', whis=1.5)    # whis ==> Length of vertical line

data = np.random.normal(size=(1000, 4), loc=0, scale=1)

labels = ['A', 'B', 'C', 'D']

plt.boxplot(data, labels=labels)

plt.show()