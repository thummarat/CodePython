import cv2
img = cv2.imread('chiba.jpg')
#r, g, b = img[0], img[1], img[2]
#cv2.imshow('Image Chiba',img)
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#cv2.imshow('Image Chiba Gray',img_gray)
img_hsv = cv2.cvtColor(img,cv2.COLOR_RGB2HSV)
#cv2.imshow('Image Chiba HSV',img_hsv)
img_rgb = cv2.cvtColor(img_gray,cv2.COLOR_GRAY2BGR)
#cv2.imshow('Image Chiba RGB',img_rgb)
#img_r, img_c = img_gray.shape
img_r, img_c = img_gray.shape
print('img r = ',img_r)
print('img c = ', img_c)
print('pixel = ',img_r * img_c)
k = img_gray
kk = img
for i in range(img_r):
    for j in range(img_c):
        k[i, j] = 0.2989*img[i,j,2] + 0.5870*img[i,j,1] + 0.1140*img[i,j,0]  #0.2989 * r + 0.5870 * g + 0.1140 * b
        kk[i,j,2] = img[i,j,2] #R
        kk[i, j, 1] = 0  # G
        kk[i, j, 0] = 0  # B
        #print(k)
cv2.imshow('Gray img',k)
#cv2.imshow('New img', kk)
cv2.waitKey(0)
cv2.destroyAllWindows()
