import numpy as np
import random as rd
import math

def initMask(frame):
  rows, cols, _ = frame.shape
  resized_rows, resized_cols = rows//10, cols//10
  return np.zeros((resized_rows, resized_cols))

### Matrix Effect

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

### Stain Effect

f_spawn = 0.1 #probability of spawn

def getRandomSpawn(mask):
  resized_rows, resized_cols = mask.shape
  return {
    'row': rd.randint(0, resized_rows-1),
    'col': rd.randint(0, resized_cols-1),
    'radius': 0
  }

def isInStain(pixel_x, pixel_y, stain):
  d = math.sqrt((pixel_x - stain['row'])**2 + (pixel_y - stain['col'])**2)
  # print(d, stain['radius'])
  return d < stain['radius']

def initStainEffect(mask):
  return {
    'stains': [getRandomSpawn(mask)]
  }

def updateStainEffect(mask, index, params):
  resized_rows, resized_cols = mask.shape

  # Probably add a stain
  if rd.random() < f_spawn:
    params['stains'].append(getRandomSpawn(mask))

  # expand stains
  for stain in params['stains']:
    stain['radius'] += 1

    rows_range =range(max(stain['row'] - stain['radius'], 0), min(stain['row'] + stain['radius'], resized_rows))
    cols_range =range(max(stain['col'] - stain['radius'], 0), min(stain['col'] + stain['radius'], resized_cols))

    for row in rows_range:
      for col in cols_range:
        if mask[row, col] == 0 and isInStain(row, col, stain):
          mask[row, col] = 1

  return mask.sum(dtype=np.int32) == resized_cols * resized_rows
