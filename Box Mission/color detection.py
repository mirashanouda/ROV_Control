import cv2
import numpy as np
import glob
from numpy.core import numeric


image_copy = cv2.imread('/Users/ranaelgahawy/Desktop/ROV/images/side1.png')

hsv = cv2.cvtColor(image_copy, cv2.COLOR_BGR2HSV)

# define range wanted color in HSV
lower_val = np.array([60, 100,50]) 
upper_val = np.array([50, 80, 70]) 

# Threshold the HSV image - any green color will show up as white
mask = cv2.inRange(hsv, lower_val, upper_val)
# cv2.imshow("Mask", mask)
# cv2.waitKey(0)

# if there are any white pixels on mask, sum will be > 0
hasGreen = np.sum(mask)
res = cv2.bitwise_and(image_copy,image_copy,mask=mask)
fin = np.hstack((image_copy,res))
if hasGreen > 0:
    print('Green detected!')
    cv2.imshow("Res", fin)
    cv2.imshow("Mask", mask)
    cv2.waitKey(0)
else:
    print('Color is not detected')

# show image 
# apply mask to image

# display image

# height, width, depth = image_copy.shape
# circle_img = np.zeros((height, width), np.uint8)

# mask = cv2.circle(circle_img, (int(width/ 3), int(height/8)), 1, 1, thickness=-1)
# masked_img = cv2.bitwise_and(image_copy, image_copy, mask=circle_img)

# circle_locations = mask == 1
# bgr = image_copy[circle_locations]

# rgb = bgr[..., ::-1]

# print(rgb)
# cv2.imshow('img', image_copy)
# cv2.imshow("masked", masked_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
