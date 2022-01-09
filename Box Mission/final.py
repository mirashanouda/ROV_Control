import cv2
import numpy as np
import glob
from numpy.core import numeric



def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

files = glob.glob ("/Users/ranaelgahawy/Desktop/ROV/images/*.png")
img = np.empty(len(files))

for i in files:
    img= cv2.imread(i)
# path = '/Users/ranaelgahawy/Desktop/ROV/top.jpg'
# img = cv2.imread(path)
    num = 0
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
    ret, thresh = cv2.threshold(imgGray, 170, 205, cv2.THRESH_BINARY)
    # cv2.imshow('Binary image', thresh)
    # cv2.waitKey(0)
    cv2.imwrite('image_thres1.jpg', thresh)
    cv2.destroyAllWindows()
    contours, hierarchy = cv2.findContours(image=thresh, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)
    image_copy = img.copy()
    height, width, channels = img.shape
    print(height, width)
    print()
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        if (area>(height*width)/50) & (area < (height*width)/2):
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.01*peri,True)
            print(len(approx))
            objCor = len(approx)
            x, y, w, h = cv2.boundingRect(approx)

            if objCor == 4:
                num = num + 1
                cv2.drawContours(image_copy, cnt, -1, (255, 0, 0), 3, lineType=cv2.LINE_AA)
                aspRatio = w/float(h)
                if aspRatio >0.95 and aspRatio <1.05: objectType= "Square"
                else:objectType="Rectangle"
                cv2.rectangle(image_copy,(x,y),(x+w,y+h),(0,255,0),2)
                cv2.putText(image_copy,objectType,
                            (x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX,0.7,
                            (0,0,0),2)

            

            



    print ("The number of objects in this image: ", num, " the height" , height, "the width" , width )

    cv2.imshow('None approximation', image_copy)
    cv2.waitKey(0)
    cv2.imwrite('contours_none_image1.jpg', image_copy)
    cv2.destroyAllWindows()
