import cv2
img = cv2.imread('char.jpg')
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#cv2.imshow('Chiba',img_gray)
new_img = img_gray
r, c = img_gray.shape
print(r)
print(c)
new_img2 = img
new_img3 = img_gray
for i in range(r):
    for j in range(c):
        #new_img[i,j] = 100
        new_img[i,j] = 0.2989*img[i,j,2] + 0.5870*img[i,j,1] + 0.1140*img[i,j,0]
        new_img2[i, j, 0] = 0
        new_img2[i, j, 1] = img[i,j,1]
        new_img2[i, j, 2] = 0
        if new_img[i,j] > 130 :
            new_img3[i,j] = 255
        else:
            new_img3[i,j] = 0
cv2.imshow('Newimg',new_img3)
cv2.waitKey(0)
cv2.destroyAllWindows()