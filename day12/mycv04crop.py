
#import cv2

#src = cv2.imread("aaa.jpg", cv2.IMREAD_COLOR)
#dst = src[100:600, 200:700].copy()

#cv2.imshow("src", src)
#cv2.imshow("dst", dst)
#cv2.waitKey()
#cv2.destroyAllWindows()

#dst = src[100:600, 200:700].copy()
#aaaaaaaa

import cv2

img = cv2.imread('aaa.jpg', cv2.IMREAD_GRAYSCALE)
img_crop = img[10:180, 150:350]
 

cv2.imshow('Test Image', img_crop)
cv2.imwrite('abc.jpg', img_crop)


cv2.waitKey(0)
cv2.destroyAllWindows()






