
import cv2

import numpy as np

font = cv2.FONT_HERSHEY_SIMPLEX

img = np.zeros((500, 800, 3), np.uint8)

img[:100, :200] = (255, 0, 0)
img[:100, 200:400] = (255, 255, 255)
img[:100, 400:600] = (128, 128, 128)
img[:100, 600:] = (64, 64, 64)
cv2.putText(img,'Azul(255, 0, 0)->',(5,55), font, 0.5,(255,255,255),1,cv2.LINE_AA)
cv2.putText(img,'B=255',(215,55), font, 1,(255, 0, 0),2,cv2.LINE_AA)
cv2.putText(img,'G=0',(415,55), font, 1,(255, 0, 0),2,cv2.LINE_AA)
cv2.putText(img,'R=0',(615,55), font, 1,(255, 0, 0),2,cv2.LINE_AA)

img[100:200, :200] = (0, 255, 0)
img[100:200, 200:400] = (128, 128, 128)
img[100:200, 400:600] = (64, 64, 64)
img[100:200, 600:] = (255, 255, 255)
cv2.putText(img,'Verde(0, 255, 0)->',(5,155), font, 0.5,(255,255,255),1,cv2.LINE_AA)
cv2.putText(img, 'B=0', (215, 155), font, 1, (0, 255, 0), 2, cv2.LINE_AA)
cv2.putText(img, 'G=255', (415, 155), font, 1, (0, 255, 0), 2, cv2.LINE_AA)
cv2.putText(img, 'R=0', (615, 155), font, 1, (0, 255, 0), 2, cv2.LINE_AA)

img[200:300, :200] = (0, 0, 255)
img[200:300, 200:400] = (64, 64, 64)
img[200:300, 400:600] = (255, 255, 255)
img[200:300, 600:] = (128, 128, 128)
cv2.putText(img,'Rojo(0, 0, 255)->',(5,255), font, 0.5,(255,255,255),1,cv2.LINE_AA)
cv2.putText(img, 'B=0', (215, 255), font, 1, (0, 0, 255), 2, cv2.LINE_AA)
cv2.putText(img, 'G=0', (415, 255), font, 1, (0, 0, 255), 2, cv2.LINE_AA)
cv2.putText(img, 'R=255', (615, 255), font, 1, (0, 0, 255), 2, cv2.LINE_AA)

img[300:400, :200] = (20, 117, 240)
img[300:400, 200:400] = (255, 255, 255)
img[300:400, 400:600] = (128, 128, 128)
img[300:400, 600:] = (64, 64, 64)
cv2.putText(img,'Naranja(20,117,240)->',(5,355), font, 0.5,(255,255,255),1,cv2.LINE_AA)
cv2.putText(img, 'B=20', (215, 355), font, 1, (20, 117, 240), 2, cv2.LINE_AA)
cv2.putText(img, 'G=117', (415, 355), font, 1, (20, 117, 240), 2, cv2.LINE_AA)
cv2.putText(img, 'R=240', (615, 355), font, 1, (20, 117, 240), 2, cv2.LINE_AA)

img[400:, :200] = (109, 45, 225)
img[400:, 200:400] = (128, 128, 128)
img[400:, 400:600] = (64, 64, 64)
img[400:, 600:] = (255, 255, 255)
cv2.putText(img,'Rosa(109, 45, 225)->',(5,455), font, 0.5,(255,255,255),1,cv2.LINE_AA)
cv2.putText(img, 'B=109', (215, 455), font, 1, (109, 45, 225), 2, cv2.LINE_AA)
cv2.putText(img, 'G=45', (415, 455), font, 1, (109, 45, 225), 2, cv2.LINE_AA)
cv2.putText(img, 'R=225', (615, 455), font, 1, (109, 45, 225), 2, cv2.LINE_AA)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
