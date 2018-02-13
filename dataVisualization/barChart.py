import numpy as np
import matplotlib.pyplot as plt

# N = 5
#
# y = [20, 10, 30, 25, 15]
#
# index = np.arange(N)
#
# #pl = plt.bar(left=index, height=y, color='red', width=0.5)
# #pl1 = plt.bar(left=0, bottom=index, width=y, color='red', height=0.5, orientation='horizontal')
#
# pl = plt.barh(left=0, bottom=index)
#
# plt.show()

# Parallel Bar Chart
# index = np.arange(4)
#
# sales_BJ = [52, 55, 63, 53]
# sales_SH = [44, 66, 55, 41]
#
# bar_width = 0.3
#
# plt.bar(index, sales_BJ, bar_width, color='b')
# plt.bar(index+bar_width, sales_SH, bar_width, color='r')
# plt.show()

# Layer Bar Chart
index = np.arange(4)

sales_BJ = [52, 55, 63, 53]
sales_SH = [44, 66, 55, 41]

bar_width = 0.3

plt.bar(index, sales_BJ, bar_width, color='b')
plt.bar(index, sales_SH, bar_width, color='r', bottom=sales_BJ)
plt.show()