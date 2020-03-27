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
