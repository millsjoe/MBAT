
import numpy as np 
import matplotlib.pyplot as plt
import imageio
import json
import sys

import pprint

images = []


language = sys.argv[1]
fileToOpen = language + ".json"
def visualise(modelArray, num):
    modelArray = np.array(modelArray, ndmin=2)
    plt.title("DLA")
    plt.matshow(modelArray)
    plt.savefig("{}_images/cluster_{}".format(language,num))
    plt.close()
    images.append(imageio.imread("{}_images/cluster_{}.png".format(language,num)))
    
with open(fileToOpen) as json_file:
    json_data = json.load(json_file)

    if (language != "C"):
        visualise(json_data['modelArray'][0],0)
        length = int(len(json_data['modelArray']))
        visualise(json_data['modelArray'][length -1 ],length-1)
    else:
        visualise(json_data['modelArray'],0)




