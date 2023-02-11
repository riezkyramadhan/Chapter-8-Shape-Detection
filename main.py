import cv2
import numpy as np 

path = "shape.jpg"
img = cv2.imread(path)
imgContour = img.copy()

def getContours(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        if area>300:
            cv2.drawContours(imgContour, cnt, -1, (255,0,0),4)
            peri = cv2.arcLength(cnt, True)
            #print(peri)
            aproxx = cv2.approxPolyDP(cnt, 0.002*peri, True)
            print(len(aproxx))
            objCor = len(aproxx)
            x, y, w, h = cv2.boundingRect(aproxx)
            print (objCor,"objcor")
            cv2.rectangle(imgContour, (x,y), (x+w,y+h), (0,255,0),2)
        
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gray,(7,7), 1)
img_canny = cv2.Canny(img_blur,50 ,50)
img_blank = np.zeros_like(img)
getContours(img_canny)

cv2.imshow("Original", img)
cv2.imshow("Blur", img_blur)
cv2.imshow("Gray", img_gray)
cv2.imshow("canny", img_canny)
cv2.imshow("blank", img_blank)
cv2.imshow("contour", imgContour)


cv2.waitKey(0)
