# -*- coding: utf-8 -*-

import cv2
import numpy as np

img = cv2.imread("/Users/robinxyuan/Downloads/openCV Learn/lena.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
# OpenCV定义的结构元素
kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))

# 腐蚀图像
eroded = cv2.erode(img, kernel)
# 显示腐蚀后的图像
cv2.imshow("Eroded Image", eroded);

# 膨胀图像
dilated = cv2.dilate(img, kernel)
# 显示膨胀后的图像
cv2.imshow("Dilated Image", dilated);

cv2.imshow("Origin", img)

# NumPy定义的结构元素
NpKernel = np.uint8(np.ones((5, 5)))
Nproded = cv2.erode(img, NpKernel)
# 显示腐蚀后的图像
cv2.imshow("Eroded by NumPy kernel", Nproded);

# 闭运算
closed = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
cv2.imshow("Close", closed)

# 开运算
opened = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
cv2.imshow("Open", opened)

cv2.waitKey(0)
cv2.destroyAllWindows()