import numpy as np
import cv2

def letterToImg(letter):
  frame = np.zeros((10, 10))
  color = (255, 255, 255)
  thickness = 1
  font = cv2.FONT_HERSHEY_PLAIN
  frame = cv2.putText(frame, letter, (0, 9), font, 1, color, thickness, cv2.LINE_AA)
  return frame

def getAsciiLetters():
  letters = []
  for i in range(256):
    letters.append(chr(i))
  return letters