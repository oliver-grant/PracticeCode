from random import *

WIDTH= 50
HEIGHT = 50

grid = []

def printGrid():
  for i in range(HEIGHT):
    line = ""
    for j in range(WIDTH):
      line = line + grid[i][j]
    print(line)


def generateLevel():
  for i in range(HEIGHT):
    grid.append([])
    for j in range(WIDTH):
      grid[i].append("0")
  printGrid()

  start_x = randint(0, WIDTH)
  start_y = randint(0, HEIGHT)
  grid[start_x][start_y] = "1"
  printGrid()
  
  prevDir = -1
  relPos  = []
  for i in range(25):
    newDir = randint(0, 4)
    pos = relPos.pop(0);
    while (prevDir == newDir):
      newDir = randint(0, 4)
    if (newDir == 0):
    elif (newDir == 1):
    elif (newDir == 2):
    else:
    
    prevDir = newDir 
  
   




generateLevel()

