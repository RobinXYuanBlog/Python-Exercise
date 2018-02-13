import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

fig = plt.figure()

ax = fig.add_subplot(111)

xy1 = np.array([0.2, 0.2])
xy2 = np.array([0.2, 0.8])   # 左下角点的位置
xy3 = np.array([0.8, 0.2])
xy4 = np.array([0.8, 0.8])

circle = mpatches.Circle(xy1, 0.1)
ax.add_patch(circle)

rect = mpatches.Rectangle(xy2, 0.2, 0.1, color='r')
ax.add_patch(rect)

polygon = mpatches.RegularPolygon(xy3, 6, 0.1, color='c')   # 坐标, 边， 半径
ax.add_patch(polygon)

ellipse = mpatches.Ellipse(xy4, 0.4, 0.2, color='y')
ax.add_patch(ellipse)

plt.axis('equal')

plt.grid()

plt.show()