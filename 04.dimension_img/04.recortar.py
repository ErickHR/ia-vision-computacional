import cv2

img = cv2.imread('image.png')

imgOut = img[20:300, 100:360]

cv2.imwrite('imagen_redimensionada.png', imgOut)

cv2.waitKey(0)
cv2.destroyAllWindows()
