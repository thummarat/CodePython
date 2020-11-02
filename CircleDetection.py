import cv2
import numpy as np

img = cv2.imread('crile.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#cv2.imshow("Circle detection", gray)
imgray = cv2.medianBlur(gray,5)
#cv2.imshow("Circle detection", imgray)
#cimg = img
circles = cv2.HoughCircles(imgray, cv2.HOUGH_GRADIENT,1,110,param1=145,param2=45,minRadius=0,maxRadius=0)
circles = np.uint16(np.around(circles))
a=0
b=0
c=0
for i in circles[0, :]:
    #out circle
    cv2.circle(img,(i[0], i[1]),i[2],(0,0,255),2)
    #center
    cv2.circle(img, (i[0], i[1]), 2, (255, 0, 0), 2)
    a=a+1
    if i[2] >= 70 :
        b=b+5
    else:
        b=b+1

cv2.putText(img,"Number of Coin = "+str(a)+" Coin = "+str(b)+" Bath",(10,50),
            cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,0,0),1)
cv2.imshow("Circle detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
