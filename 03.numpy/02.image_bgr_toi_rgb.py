import cv2

import numpy as np

img = cv2.imread( 'image.png' )

# tridimensional
CB = img[ :, :, 0] #solo la primera capa
CG = img[ :, :, 1 ] #solo la segunda capa
CR = img[ :, :, 2 ] #solo la tercera capa

cv2.imshow('BGR', np.hstack( [ CB, CG, CR ] ))

#invertir las capas BGR a RGB
imgRGB = cv2.cvtColor( img, cv2.COLOR_BGR2RGB )
CB = imgRGB[ :, :, 0]
CG = imgRGB[ :, :, 1 ]
CR = imgRGB[ :, :, 2 ]

cv2.imshow('RGB', np.hstack( [ CB, CG, CR ] ))

cv2.waitKey(0)
cv2.destroyAllWindows()
