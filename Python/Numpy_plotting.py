from beginMovement import beginMovement
import numpy as np 
import random
import math
import sys
import json
import time

inputsize = int(sys.argv[1])
counterLimit = (inputsize*0.2) * (inputsize*0.2)

beginTime = time.time()

matrix = np.zeros((inputsize, inputsize))

randomX = (inputsize/2) + random.randint(0,1)
randomX = math.ceil(randomX)

randomY = (inputsize/2) + random.randint(0,1)
randomY = math.ceil(randomY)

matrix[randomX][randomY] = 1

    """ 
    Main diffusion occurs here. Intended to be completed in an iterative style
    param matrix:       Current state of the environment
    param foundCount:   Number of found cells
    """
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
        # allow for 400000 walks - should be more than enough
        if (counter == 400000 or end == True):
            break

    if foundCell:
        matrix[location[0]][location[1]] = 1
        foundCount += 1

    return (matrix, foundCount)

# use if wish to create a gif
images = []

arrayIterations = []
foundCount = 0
while(foundCount < counterLimit):
    matrix,foundCount = Diffuse(matrix,foundCount)
    
jsonDict = {}
jsonDict['modelArray'] = matrix.tolist()

# calculate time to run
time_taken = time.time() - beginTime

# log performance
result = open("../Results/Python_results.csv", "a+")
result.write("Python,{},{:.5f}\n".format(inputsize, time_taken))

# create json file of model
f = open("../JSON/Python_{}.json".format(inputsize), "w")
f.write(json.dumps(jsonDict))
f.close()
