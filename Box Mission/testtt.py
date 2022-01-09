import cv2
import numpy as np

# img = cv2.imread("/Users/ranaelgahawy/Desktop/ROV/top.png")

# width,height = 250,350
# pts1 = np.float32([[111,219],[287,188],[154,482],[352,440]])
# pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
# matrix = cv2.getPerspectiveTransform(pts1,pts2)
# imgOutput = cv2.warpPerspective(img,matrix,(width,height))


# cv2.imshow("Image",img)
# cv2.imshow("Output",imgOutput)

# cv2.waitKey(0)

path = '/Users/ranaelgahawy/Desktop/ROV/side2.png'
img = cv2.imread(path)
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
ret, thresh = cv2.threshold(imgGray, 170, 205, cv2.THRESH_BINARY)
cv2.imshow('Binary image', thresh)
cv2.waitKey(0)
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
    if (area>(height*width)/100) & (area < (height*width)/2):
        peri = cv2.arcLength(cnt,True)
        #print(peri)
        approx = cv2.approxPolyDP(cnt,0.01*peri,True)
        print(len(approx))
        objCor = len(approx)
        x, y, w, h = cv2.boundingRect(approx)

        if objCor == 4:
            #cv2.drawContours(image_copy, contours,contourIdx=-1, color=(0,0,255), thickness=2, lineType=cv2.LINE_AA,hierarchy=hierarchy)
            cv2.drawContours(image_copy, cnt, -1, (255, 0, 0), 3, lineType=cv2.LINE_AA)
            aspRatio = w/float(h)
            if aspRatio >0.95 and aspRatio <1.05: objectType= "Square"
            else:objectType="Rectangle"
            cv2.rectangle(image_copy,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(image_copy,objectType,
                        (x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX,0.7,
                        (0,0,0),2)

        



        

cv2.imshow('None approximation', image_copy)
cv2.waitKey(0)
cv2.imwrite('contours_none_image1.jpg', image_copy)
cv2.destroyAllWindows()
# for cnt in contours:
#     area = cv2.contourArea(cnt)
#     print(area)
#     if area >500 :
