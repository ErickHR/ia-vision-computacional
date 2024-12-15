import cv2
import numpy as np

img = cv2.imread("image.png")

height, width = img.shape[:2]

M = np.float32([[1,0,width/2],[0,1,height/2]])

dst = cv2.warpAffine(img, M, (width, height))

cv2.imwrite("imagen_trasladada2.png", dst)

# cv2.imshow("Imagen de entrada", img) 
# cv2.imshow("Imagen de salida", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()