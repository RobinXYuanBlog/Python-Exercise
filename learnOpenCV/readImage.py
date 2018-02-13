#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 23:08:36 2017

@author: robinxyuan
"""

import cv2

# Load image
img = cv2.imread("/Users/robinxyuan/Downloads/openCV Learn/lena.png")

# Create window
cv2.namedWindow("Image")

# Show image in the window
cv2.imshow("Image", img)
cv2.waitKey(0)

cv2.destroyAllWindows()