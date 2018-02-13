# -*- coding: utf-8 -*-

import cv2
import numpy as np

# Load image
img = cv2.imread("/Users/robinxyuan/Downloads/openCV Learn/lena.png")

# Create a new empty image
emptyImage = np.zeros(img.shape, np.uint8)

# Copy image
emptyImage2 = img.copy()
  

emptyImage3 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  
#emptyImage3[...]=0  # Transfer image to gray

# Show images
cv2.imshow("EmptyImage", emptyImage)  
cv2.imshow("Image", img)  
cv2.imshow("EmptyImage2", emptyImage2)  
cv2.imshow("EmptyImage3", emptyImage3)  

cv2.waitKey(0)
cv2.destroyAllWindows()

