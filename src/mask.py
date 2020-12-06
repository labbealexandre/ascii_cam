import numpy as np
import random as rd

def initMask(frame):
  rows, cols, _ = frame.shape
  resized_rows, resized_cols = rows//10, cols//10
  return np.zeros((resized_rows, resized_cols))

def initMatrixEffect(mask):
  resized_rows, resized_cols = mask.shape
  indexes = np.array([-rd.randint(0, resized_rows-1) for i in range(resized_cols)])
  return {
    'indexes': indexes
  }

def updateMatrixEffect(mask, index, params):
  resized_rows, resized_cols = mask.shape

  for col in range(resized_cols):
    row = params['indexes'][col]
    if row >= 0 and row < resized_rows:
      mask[row, col] = 1
  
  params['indexes'] = params['indexes'] + np.ones(resized_cols, dtype=int)
  return np.min(params['indexes']) >= resized_rows
