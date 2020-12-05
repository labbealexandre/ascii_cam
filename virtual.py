import numpy as np
import cv2
import pyfakewebcam

from src import filters as ft

cap = cv2.VideoCapture(0)
ret, frame = cap.read()
h, w = frame.shape[:2]

stream_camera = pyfakewebcam.FakeWebcam(
    "/dev/video1", w, h
)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    outputFrame = ft.asciiFilter(frame)

    # Display the resulting frame
    cv2.imshow('frame',outputFrame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    stream_camera.schedule_frame(outputFrame[..., ::-1])

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
