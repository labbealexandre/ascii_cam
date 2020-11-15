import numpy as np
import cv2

cap = cv2.VideoCapture(0)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 160)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 90)

from src import filters as ft

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    outputFrame = ft.edgesFilter(frame)

    # Display the resulting frame
    cv2.imshow('frame',outputFrame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()