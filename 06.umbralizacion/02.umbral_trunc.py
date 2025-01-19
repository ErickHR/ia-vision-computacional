import cv2
import numpy as np

img = np.zeros((500, 600, 3), dtype=np.uint8)

img[100:300, :200] = 130
img[100:300, 200: 400] = 20
img[100:300, 400:] = 210

img[300:, :200] = 35
img[300:, 200:400] = 255
img[300:, 400:] = 70

font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'Umbral: T=130', (100, 70), font, 1.5, (255, 255, 255), 2, cv2.LINE_AA)


imgCopy = img.copy()
#toma el valor del umbral, el valor 130 es ignorado
_, trunc = cv2.threshold(imgCopy, 70, 130, cv2.THRESH_TRUNC)

cv2.imshow('imagen', np.hstack([img, trunc]))

cv2.waitKey(0)
cv2.destroyAllWindows()
