import cv2
import numpy as np

def cannyThreshold(lowThreshold):
    detected_edge = cv2.GaussianBlur(gray, (3, 3), 0)
    detected_edge = cv2.Canny(detected_edge, lowThreshold, lowThreshold * ratio,
                              apertureSize=kernel_size)
    dst = cv2.bitwise_and(img, img, mask=detected_edge) # just add some colors to edge from original image
    cv2.imshow("Canny Demo", dst)

lowThreshold = 0
max_lowThreshold = 100
ratio = 3
kernel_size = 3

img = cv2.imread("/Users/robinxyuan/Downloads/openCV Learn/lena.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.namedWindow("Canny Demo")

cv2.createTrackbar("Min threshold", "Canny Demo", lowThreshold, max_lowThreshold, cannyThreshold)

cannyThreshold(0)
if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()