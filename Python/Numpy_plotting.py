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
    # mark a border 
    for i in range(inputsize - 1):
        matrix[0][i] = 2
        matrix[inputsize - 1][i] = 2
        matrix[i][0] = 2
        matrix[i][inputsize - 1] = 2
        matrix[inputsize - 1][inputsize - 1] = 2
