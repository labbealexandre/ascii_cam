"""Edges filter main module."""

import cv2  # type: ignore

from src import filters as ft
from src import capture as cp
from src import engine as eg

FRAME_NAME = 'frame'

cap = cv2.VideoCapture(0)
cp.set_full_screen(FRAME_NAME)
frame = cap.read()[1]

try:
    eg.run(cap, FRAME_NAME, ft.edges_filter)
except RuntimeError:
    pass

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
