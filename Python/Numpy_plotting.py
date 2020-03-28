from beginMovement import beginMovement
from matplotlib import colors 
from pygifsicle import optimize
import numpy as np 
import matplotlib.pyplot as plt
import random
import math
import imageio
import sys
import json

inputsize = int(sys.argv[1])
counterLimit = int(sys.argv[2])

matrix = np.zeros((inputsize, inputsize))

randomX = (inputsize/2) + random.randint(0,1)
randomX = math.ceil(randomX)

randomY = (inputsize/2) + random.randint(0,1)
randomY = math.ceil(randomY)

matrix[randomX][randomY] = 1

def randomCornerStart():
    decider = random.randint(0,3)

    if decider == 0:
        randomX = 2
        randomY = 2
    elif decider == 1:
        randomX = 2
        randomY = inputsize - 1
    elif decider == 2:
        randomX = inputsize - 1
        randomY = 2
    elif decider == 3:
        randomX = inputsize - 1
        randomY = inputsize - 1

    return randomX,randomY

def doTheThing(matrix, foundCount):
    startRandomX = random.randint(1,inputsize - 1)
    startRandomY = random.randint(1,inputsize - 1)

    # startRandomX,startRandomY = randomCornerStart()

    location = [startRandomX, startRandomY]

    # matrix[location[0]][location[1]] = 1

    # mark a border 
    for i in range(inputsize - 1):
        matrix[0][i] = 2
        matrix[inputsize - 1][i] = 2
        matrix[i][0] = 2
        matrix[i][inputsize - 1] = 2
        matrix[inputsize - 1][inputsize - 1] = 2

    foundCell = False
    nearEdge = False
    counter = 0
    while (foundCell == False and nearEdge == False):
        location,foundCell, nearEdge, end = beginMovement(location,matrix,inputsize)
        counter += 1
        if (counter == 400000 or end == True):
            break

    if foundCell:
        matrix[location[0]][location[1]] = 1
        foundCount += 1

    return (matrix, foundCell,foundCount)

images = []

arrayIterations = []
foundCount = 0
while(foundCount < counterLimit):
    matrix,foundCell,foundCount = doTheThing(matrix,foundCount)
    if foundCell:
        arrayIterations.append(matrix.tolist())

jsonDict = {}
jsonDict['modelArray'] = arrayIterations

# jsonloadedDict = json.dumps(jsonDict)

f = open("Python.json", "w")
f.write(json.dumps(jsonDict))
f.close()
