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

params = mk.initMatrixEffect(mask)
isFinished = False

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    if not isFinished:
        isFinished = mk.updateMatrixEffect(mask, index, params)
        index +=1

    outputFrame = ft.asciiFilter(frame, mask=mask, q=1.6)

    # Display the resulting frame
    cv2.imshow('frame',outputFrame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
