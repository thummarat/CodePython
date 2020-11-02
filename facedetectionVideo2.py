import cv2
face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_eye.xml')
#img=cv2.imread('face.jpg')
#gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#faces=face_cascade.detectMultiScale(gray,1.1,4)

#for (x,y,w,h) in faces:
#    cv2.rectangle(img, (x,y),(x+w, y+h), (255,0,0),3)

#cv2.imshow('Face detection',img)
#cv2.waitKey()

cap = cv2.VideoCapture(0)
while (True) :
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    eye = eye_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
    for (x, y, w, h) in eye:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

    cv2.imshow('Detection', frame)
    if(cv2.waitKey(1) & 0xFF==ord('q')) :
        break
cap.release()
cv2.destroyAllWindows()