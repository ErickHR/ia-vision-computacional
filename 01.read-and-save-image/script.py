import cv2

imagen = cv2.imread('image.png', 0)

cv2.imwrite('image_copy.png', imagen)



while True:
  cv2.imshow('Lanscape', imagen)
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

cv2.destroyAllWindows()

