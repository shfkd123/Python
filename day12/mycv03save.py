import cv2

img = cv2.imread('aaa.jpg', cv2.IMREAD_GRAYSCALE) 

cv2.imwrite('abc.jpg', img)

print(img)

cv2.imshow('Test Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

