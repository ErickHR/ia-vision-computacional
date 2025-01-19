
import cv2

cap = cv2.VideoCapture(0)

while cap.isOpened():
  ret, img = cap.read()
  if ret != True:
    break

  widthMiddle = img.shape[1] // 2
  
  img[:, :widthMiddle] = cv2.flip(img[:, widthMiddle:], 1)

  cv2.imshow('video', img )


  img[:, widthMiddle:] = cv2.flip(img[:, :widthMiddle], 1)
  cv2.imshow('video_', img )

  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

cap.release()
cv2.destroyAllWindows()