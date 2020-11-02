import cv2
img = cv2.imread("Dino.jpg",0)
cv2.imshow('Show Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("Dinogray.jpg",img)
