import cv2

img = cv2.imread("image.png")

height, width = img.shape[:2]

rotate = 0

while True:
    M = cv2.getRotationMatrix2D((width / 2, height / 2), rotate, 1)
    dst = cv2.warpAffine(img, M, (width, height))
    # cv2.imwrite("imagen_rotada.png", dst)

    cv2.imshow("Imagen de salida", dst)
    rotate += 1
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# cv2.imshow("Imagen de entrada", img)
# cv2.imshow("Imagen de salida", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
