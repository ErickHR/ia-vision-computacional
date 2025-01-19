import cv2

img = cv2.imread("image.png")

# flip0 = cv2.flip(img, 1)
# flip0 = cv2.flip(img, 0)
flip0 = cv2.flip(img, -1)

cv2.imwrite("imagen_invertida.png", flip0)

cv2.waitKey(0)
cv2.destroyAllWindows()
