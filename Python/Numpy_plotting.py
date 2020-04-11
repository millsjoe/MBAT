from beginMovement import beginMovement
import numpy as np 
import random
import math
import sys
import json

inputsize = int(sys.argv[1])
counterLimit = (inputsize*0.4) * (inputsize*0.1)

matrix = np.zeros((inputsize, inputsize))

randomX = (inputsize/2) + random.randint(0,1)
randomX = math.ceil(randomX)

randomY = (inputsize/2) + random.randint(0,1)
randomY = math.ceil(randomY)

matrix[randomX][randomY] = 1

def Diffuse(matrix, foundCount):
    startRandomX = random.randint(1,inputsize - 1)
    startRandomY = random.randint(1,inputsize - 1)

    location = [startRandomX, startRandomY]

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
    matrix,foundCell,foundCount = Diffuse(matrix,foundCount)
    if foundCell:
        arrayIterations.append(matrix.tolist())

jsonDict = {}
jsonDict['modelArray'] = arrayIterations

f = open("Python.json", "w")
f.write(json.dumps(jsonDict))
f.close()
