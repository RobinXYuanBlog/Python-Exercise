import cv2
import numpy as np

# img = cv2.imread("/Users/robinxyuan/Downloads/openCV Learn/lena.png")

# calc histgram
# cv2.calcHist(img,
#              [0],              # channel
#              None,             # mask
#              [256],            # hist size
#              [0.0, 255.0])     # hist area of pillars

# histgram of RGB
# b, g, r = cv2.split(img)

# Method 1, split channels and draw r, g, b respectively

# Define a function for calculating and draw hist
# def calcAndDrawHist(image, color):
#     hist = cv2.calcHist([image], [0], None, [256], [0.0, 255.0])
#     minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(hist)
#     histImage = np.zeros([256, 256, 3], np.uint8)
#     hpt = int(0.9 * 256)
#
#     for h in range(256):
#         intensity = int(hist[h] * hpt / maxVal)
#         cv2.line(histImage, (h, 256), (h, 256-intensity), color)
#
#     return histImage
#
#
# if __name__ == '__main__':
#     img = cv2.imread("/Users/robinxyuan/Downloads/openCV Learn/lena.png")
#     b, g, r = cv2.split(img)
#
#     histImgB = calcAndDrawHist(b, [255, 0, 0])
#     histImgG = calcAndDrawHist(g, [0, 255, 0])
#     histImgR = calcAndDrawHist(r, [0, 0, 255])
#
#     cv2.imshow("hisImgB", histImgB)
#     cv2.imshow("hisImgG", histImgG)
#     cv2.imshow("hisImgR", histImgR)
#
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

# Method 2, draw r, g, b in one graph
img = cv2.imread("/Users/robinxyuan/Downloads/openCV Learn/lena.png")
h = np.zeros((256, 256, 3)) # Create the graph for drawing hist

bin = np.arange(256).reshape(256, 1)  # every bin peak in hist
color = ((255, 0, 0), (0, 255, 0), (0, 0, 255)) # BGR

for ch, col in enumerate(color):
    originHist = cv2.calcHist([img], [ch], None, [256], [0, 256])  # Get the hist of three channels
    # Use the normalize function built in openCV to limit the area of hist from 0 to 0.9*255
    cv2.normalize(originHist, originHist, 0, 255*0.9, cv2.NORM_MINMAX)
    # Transfer float to integer in originHist graph, int32 is required
    hist = np.int32(np.around(originHist))
    # Transfer bin value to coordinate, np.column_stack set array to [bin, hist] shape
    pts = np.column_stack((bin, hist))
    # Draw the hist
    cv2.polylines(h, [pts], False, col)

# Transfer the orientation of hist, since (0, 0) is in the northwest corner
h = np.flipud(h)

cv2.imshow('colorHist', h)
cv2.waitKey(0)

