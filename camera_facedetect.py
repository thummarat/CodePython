import cv2

faceCascade=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

def draw_boundary(img,classifier,scalFactor,minNeighbors,color,text):
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    features=classifier.detecMultiScale(gray,scalFactor,minNeighbors)
    coords=[]
    for (x,y,w,h) in features:
        cv2.rectangle(img,(x,y),(x+w),(y+h),color,2)
        cv2.putText(img,text,(x,y-4),cv2.FONT_HERSHEY_SIMPLEX,0.8,color,1)
    return img

def detect(img,faceCascade):
    img=draw_boundary(img,faceCascade,1.1,3,(255,0,0),"Face")
    return img

cap = cv2.VideoCapture("Video.mp4")
while (True) :
    ret,frame = cap.read()
    frame=detect(frame,faceCascade)
    cv2.imshow('frame',frame)
    if(cv2.waitKey(1) & 0xFF==ord('q')) :
        break
cap.release()
cv2.destroyAllWindows()

