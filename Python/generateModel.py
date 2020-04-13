
import numpy as np 
import matplotlib.pyplot as plt
import imageio
import json
import sys
import collections
import pprint

images = []
model_arrays = []
occupied = []


def visualise(modelArray, num):
    modelArray = np.array(modelArray, ndmin=2)
    plt.title("DLA")
    plt.matshow(modelArray)
    plt.savefig("{}_images/cluster_{}".format(language,num))
    plt.close()
    images.append(imageio.imread("{}_images/cluster_{}.png".format(language,num)))

    

def fractalCalc(modelArray):
    modelArray = np.array(modelArray)
    num_ones = (modelArray == 1).sum()
    num_zero = (modelArray == 0).sum()
    num_two = (modelArray == 2).sum()
    total = num_ones + num_two + num_zero
    size = int(np.sqrt(total))
    
    model_arrays.append(size)
    occupied.append(num_ones)
    
    

def plotFractal():


    for file in files:
        fileToOpen = "../JSON/" + language + "_" + str(file) + ".json"
        with open(fileToOpen) as json_file:
            json_data = json.load(json_file)
            fractalCalc(json_data['modelArray'])

    logRadius=np.log(model_arrays)
    logMass=np.log(occupied)

    #Fit a log function using numpy polyfit
    fitLog=np.polyfit(logRadius, logMass,1)
    fitLogFunc=np.poly1d(fitLog)

    num= np.round(fitLog[0],2)

    errorMargin = np.round(((num - 1.70)/1.70) * 100, 2)
    fig = plt.figure()
    fig.text(0.4,0.2,"Fractal dimension: " + str(num))
    fig.text(0.4,0.165,"DLA Estimate: 1.70~")
    fig.text(0.4,0.135,"Error of calculated dimension: " + str(errorMargin) + "%")

    plt.scatter(logRadius,logMass, color='red')
    plt.plot(logRadius, fitLogFunc(logRadius),color='blue')
    plt.title("Mass vs Radius (log to log) ")
    plt.xlabel("Log radius")
    plt.ylabel("Log mass")
    plt.show()

option = sys.argv[1]
language = sys.argv[2]


if (option == "--fractal"):
    start = int(sys.argv[3])
    end = int(sys.argv[4])
    increment = int(sys.argv[5])
    files = np.arange(start,end,increment)
    plotFractal()

elif (option == "--model"):
    num = int(sys.argv[3])
    fileToOpen = "../JSON/" + language + "_" + str(num) + ".json"
    with open(fileToOpen) as json_file:
            json_data = json.load(json_file)
            visualise(json_data['modelArray'],num)

