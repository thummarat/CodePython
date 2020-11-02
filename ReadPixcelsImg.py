import cv2
#import numpy as np

img = cv2.imread("imges/chiba.jpg")
cv2.imshow('Image',img)

#img_color = cv2.imread(img)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
im_r, im_c = img_gray.shape
cv2.imshow('Image Gray',img_gray)
edges = cv2.Canny(img_gray,100,200)
cv2.imshow('Edges',edges)

print('RGB shape : ', img.shape)
print('Gray shape : ', img_gray.shape)
print('r : ', im_r)
print('c : ', im_c)
print('Img size : ', img_gray.size)

cv2.waitKey(0)
cv2.destroyAllWindows()