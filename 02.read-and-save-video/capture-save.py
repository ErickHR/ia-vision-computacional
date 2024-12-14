# capturar video in camera and save

import cv2

cap = cv2.VideoCapture(0)
video = cv2.VideoWriter('camera.avi',cv2.VideoWriter_fourcc(*'XVID'),20.0,(640,480))

while(cap.isOpened()):
  ret, frame = cap.read()
  if ret != True:
    break

  cv2.imshow('frame', frame)
  video.write(frame)

  if cv2.waitKey(30) & 0xFF == ord('q'):
    break

cap.release()
video.release()

cv2.destroyAllWindows()
