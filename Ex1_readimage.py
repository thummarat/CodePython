import cv2
img = cv2.imread("chiba.jpg")
cv2.imshow("Image",img)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", img_gray)
img_hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
cv2.imshow("HSV", img_hsv)
r,c = img.shape[:2]
resize_img = cv2.resize(img, (int(r*50/100),int(c*50/100)), interpolation=cv2.INTER_AREA)
cv2.imshow("Resize",resize_img)
img_crop = img[100:100+500, 100:100+500]
#[y:y+h, x:x+w]
#img_crop = img[10:100, 100:100]
cv2.imshow("Crop", img_crop)
cv2.waitKey(0)
cv2.destroyAllWindows()