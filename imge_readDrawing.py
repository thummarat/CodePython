import cv2
img=cv2.imread('Dog1.jpg')
img=cv2.line(img,(0,0),(255,255),(255,0,0),5)
img=cv2.arrowedLine(img,(0,0),(300,200),(255,0,0),5)
img=cv2.rectangle(img,(100,100),(200,250),(0,0,255),2)
img=cv2.circle(img,(80,80),60,(0,255,0),2)
img=cv2.putText(img,"Dog name : Peakman",(10,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2)
cv2.imshow('Image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()