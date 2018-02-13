import cv2
import numpy as np

## Could denoise before using laplacian

img = cv2.imread("/Users/robinxyuan/Downloads/openCV Learn/lena.png", 0)

gray_lap = cv2.Laplacian(img, cv2.CV_16S, ksize=3)
dst = cv2.convertScaleAbs(gray_lap)

cv2.imshow("Laplacian", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()