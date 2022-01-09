import cv2
import numpy as np
import glob
from numpy.core import numeric

files = glob.glob ("/Users/ranaelgahawy/Desktop/ROV/images/*.png")
images = np.empty(len(files))

    
for i in files:
    images= cv2.imread(i)
    # cv2.imshow('myFile'+str(i),images)


cv2.imshow('test', images[0])
cv2.waitKey(0)