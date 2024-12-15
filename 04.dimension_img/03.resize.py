import cv2
import imutils

img = cv2.imread('image.png')

# img = cv2.resize(img, (500,800), interpolation=cv2.INTER_CUBIC)

imgOut = imutils.resize(img, height=300, width=200)
# imgOut = imutils.resize(img, width=200)

cv2.imwrite('imagen_redimensionada.png', imgOut)
cv2.waitKey(0)
cv2.destroyAllWindows()