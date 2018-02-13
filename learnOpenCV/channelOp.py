import cv2
import numpy as np

img = cv2.imread("/Users/robinxyuan/Downloads/openCV Learn/lena.png")

# Channel split
## Method 1
blue, green, red = cv2.split(img)
cv2.imwrite("/Users/robinxyuan/Downloads/openCV Learn/lenaBlue.png", blue)
cv2.imwrite("/Users/robinxyuan/Downloads/openCV Learn/lenaGreen.png", green)
cv2.imwrite("/Users/robinxyuan/Downloads/openCV Learn/lenaRed.png", red)

## Method 2
# b = np.zeros((img.shape[0], img.shape[1]), dtype=img.dtype)
# g = np.zeros((img.shape[0], img.shape[1]), dtype=img.dtype)
# r = np.zeros((img.shape[0], img.shape[1]), dtype=img.dtype)
#
# b[:, :] = img[:, :, 0]
# g[:, :] = img[:, :, 1]
# r[:, :] = img[:, :, 2]
#
# cv2.imwrite("/Users/robinxyuan/Downloads/openCV Learn/lenaBlue.png", b)
# cv2.imwrite("/Users/robinxyuan/Downloads/openCV Learn/lenaGreen.png", g)
# cv2.imwrite("/Users/robinxyuan/Downloads/openCV Learn/lenaRed.png", r)

# Channel merge
## Method 1
merged = cv2.merge([blue, green, red])
print "Merge by OpenCV"
print merged.strides

mergedByNp = np.dstack([blue, green, red])
print "Merge by NumPy "
print mergedByNp.strides

cv2.waitKey(0)
cv2.destroyAllWindows()
