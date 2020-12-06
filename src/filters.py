import cv2
import numpy as np

def grayFilter(frame):
  return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

def reductionFilter(frame):

  def my_round(pixel):
    new_pixel = np.round(pixel / 32) * 32
    return new_pixel.astype(np.uint8)

  output = grayFilter(frame)
  rows, cols = output.shape
  output = my_round(output)

  return output

def sandboxFilter(frame):
  org = (50, 50)
  color = (255, 255, 255)
  thickness = 1
  font = cv2.FONT_HERSHEY_PLAIN 
  outputFrame = cv2.putText(frame, 'a', org, font, 1, color, thickness, cv2.LINE_AA)
  size = cv2.getTextSize('a', font, 1, 1)
  return outputFrame

def asciiFilter(frame, isGrey=False, mask=None, q=1):
  ascii_char = [' ','.',':','-','=','+','*','o','%','#']
  n = 256 / len(ascii_char)
  color = (1, 1, 1)
  thickness = 1
  font = cv2.FONT_HERSHEY_PLAIN

  if isGrey:
    _frame = frame
  else:
    _frame = grayFilter(frame)

  rows, cols = _frame.shape
  output = np.zeros((rows, cols, 3))

  resized_rows, resized_cols = rows//10, cols//10
  _frame = cv2.resize(_frame, (resized_cols, resized_rows), interpolation = cv2.INTER_LINEAR)

  def round(pixel):
    new_pixel = np.floor((pixel / n) / q)
    return new_pixel.astype(np.uint8)

  _frame = round(_frame)
  
  for i in range(resized_rows):
    for j in range(resized_cols):
      if mask is not None and mask[i,j] == 1:
        output = cv2.putText(output, ascii_char[_frame[i, j]], (j*10, i*10+9), font, 1, color, thickness, cv2.LINE_AA)
      else:
        output[i*10:(i+1)*10,j*10:(j+1)*10] = frame[i*10:(i+1)*10,j*10:(j+1)*10]/256.0

  return output

def edgesFilter(frame):
  gray = grayFilter(frame)
  gray_filtered = cv2.bilateralFilter(gray, 7, 50, 50)
  # output = cv2.Canny(gray_filtered, 40, 80)
  output = cv2.Canny(gray_filtered, 20, 30)

  return output