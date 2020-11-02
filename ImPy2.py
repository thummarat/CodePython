import cv2
img = cv2.imread("Dino.jpg")
print(type(img))
cv2.imshow("Original image",img)
cv2.waitKey(0)
