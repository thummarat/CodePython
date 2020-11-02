import cv2
face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_eye.xml')

img=cv2.imread('face.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces=face_cascade.detectMultiScale(gray,1.3,5)

for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y),(x+w, y+h), (0,255,255),2)

#cv2.imshow('Face detection',img)

eye=eye_cascade.detectMultiScale(gray,1.3,5)

for (x,y,w,h) in eye:
    cv2.rectangle(img, (x,y),(x+w, y+h), (0,0,255),2)

#cv2.imshow('eye detection',img)
cv2.imshow('face and eye detection',img)
cv2.waitKey(0)
cv2.destroyAllWindows()