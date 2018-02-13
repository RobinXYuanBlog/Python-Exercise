import cv2
import numpy as np

######################################
# Create the phenomenon on the image #
# img: image path                    #
# n: the number of snow flower       #
######################################
def snow(img, n):
    for k in range(n):
        i = int(np.random.random() * img.shape[0])
        j = int(np.random.random() * img.shape[1])
        # Gray-scale image
        if img.ndim == 2:
            img[i, j] = 255
        # Colorful image
        if img.ndim == 3:
            # The final numbers (0,1,2) reprenst channel
            img[i, j, 0] = 255
            img[i, j, 1] = 255
            img[i, j, 2] = 255
    return img


if __name__ == '__main__':
    img = cv2.imread("/Users/robinxyuan/Downloads/openCV Learn/lena.png")
    snowImage = snow(img, 500)
    cv2.imwrite("/Users/robinxyuan/Downloads/openCV Learn/lenaSnow.png", snowImage)
    cv2.waitKey(0)
    cv2.destroyAllWindows()