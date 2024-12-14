
import cv2

cap = cv2.VideoCapture('camera.avi')

while( cap.isOpened() ):
  ret, frame = cap.read()
  if ret != True:
    break

  cv2.imshow('frame', frame)

  # por que 30 y no 1, es para apreciar el video mas lento
  if cv2.waitKey(30) & 0xFF == ord('q'):
    break

cap.release()
cv2.destroyAllWindows()
