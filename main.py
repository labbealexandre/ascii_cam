import numpy as np
import cv2

cap = cv2.VideoCapture(0)

from src import filters as ft
from src import utils as ut
from src import mask as mk

ret, frame = cap.read()

index = 0
mask = mk.initMask(frame)
resized_rows, resized_cols = mask.shape

params = mk.initStainEffect(mask)
isStarted, isFinished = False, False

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    if not isFinished and isStarted:
        isFinished = mk.updateStainEffect(mask, index, params)
        index +=1

    outputFrame = ft.asciiFilter(frame, mask=mask, q=1.6)

    # Display the resulting frame
    cv2.imshow('frame',outputFrame)
    key_pressed = cv2.waitKey(1) & 0xFF
    if key_pressed == ord('q'):
        break
    if key_pressed == ord('m'):
        isStarted = True

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
