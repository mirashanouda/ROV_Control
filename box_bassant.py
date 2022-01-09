import cv2
import numpy as np

hue = np.zeros((5,))
sat = np.zeros((5,))
val = np.zeros((5,))
centersX = np.zeros((4,), dtype=int)
centersY = np.zeros((4,), dtype=int)


def getTopContours(img, imgHSV):
    contours, hierarchy = cv2.findContours(
        img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    p = 0
    for cnt in contours:
        # cv2.drawContours(img, cnt, -1, (255, 0, 0), 3)
        # peri = cv2.arcLength(cnt, 1)
        # approx = cv2.approxPolyDP(cnt, 0.02*peri, 1)
        x, y, w, h = cv2.boundingRect(cnt)

        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        # cv2.imshow('test', topContour)
        cv2.putText(img, str(p),
                    (x + (w // 2), y + (h // 2)), cv2.FONT_HERSHEY_COMPLEX, 0.3,
                    (0, 0, 0), 1)
        # print("{}  {}".format((x + (w // 2)-1), (y + (h // 2))))
        centersX[p] = int(x + (w // 2))
        centersY[p] = int(y + (h // 2))
        p += 1

    sortedidx = []
    # getting the hsv of the first (leftmost)
    temp = np.where(centersX == np.amin(centersX))
    idx = temp[0][0]
    sortedidx.append(idx)
    temp = np.where(centersY == np.amax(centersY))
    idx = temp[0][0]
    sortedidx.append(idx)
    temp = np.where(centersX == np.amax(centersX))
    idx = temp[0][0]
    sortedidx.append(idx)
    temp = np.where(centersY == np.amin(centersY))
    idx = temp[0][0]
    sortedidx.append(idx)
    for k in range(4):
        i = sortedidx[k]
        (hue[k], sat[k], val[k]) = imgHSV[centersY[i]][centersX[i]]


def match():
    for x in range(4):
        h = hue[x]
        s = sat[x]
        v = val[x]
        h_min = h - 10
        h_max = h + 10
        s_min = s - 10
        s_max = s + 10
        v_min = v - 10
        v_max = v + 10
        lower = np.array([h_min, s_min, v_min])
        upper = np.array([h_max, s_max, v_max])
        for i in down:
            mask = cv2.inRange(i, lower, upper)
            # res = cv2.bitwise_and(i, i, mask=mask)
            if mask.any():
                downArr.append(i)


top = cv2.imread("1.png")
down = []
downArr = []
left = cv2.imread("2.png")
down.append(left)
right = cv2.imread("3.png")
down.append(right)
mleft = cv2.imread("4.png")
down.append(mleft)
mright = cv2.imread("5.png")
down.append(mright)

print(left.shape[1])
print(right.shape[1])

topCanny = cv2.Canny(top, 50, 50)
topHSV = cv2.cvtColor(top, cv2.COLOR_BGR2HSV)


getTopContours(topCanny, top)
match()

print("size")
print(len(downArr))

leftBlack = np.zeros_like(downArr[0])
rightBlack = np.zeros_like(downArr[3])

result = np.zeros((190, 790, 3), np.uint8)
cur_x = leftBlack.shape[1] + 10
cur_y = 0
result[:top.shape[0], cur_x:cur_x + top.shape[1]] = top
cur_y = 85
cur_x = 0
for i in range(4):
    result[cur_y:cur_y+downArr[i].shape[0],
           cur_x:cur_x+downArr[i].shape[1]] = downArr[i]
    cur_x = cur_x+downArr[i].shape[1]

cv2.imshow("Canny", topCanny)
#cv2.imshow("Contour", topContour)
cv2.imshow("result", result)
cv2.waitKey(0)
