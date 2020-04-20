import os 
import numpy
import sys
import csv
import numpy
import matplotlib.pyplot as plt
import pprint
start = int(sys.argv[1])
end = int(sys.argv[2])
increment = int(sys.argv[3])
num_runs = int(sys.argv[4])
data_range = numpy.arange(start,end,increment)

bigDict = {}

languagesdict = {}
    

languageToUse = {
    "Python" : "python3 ../Python/Numpy_plotting.py ",
    "CP" : "../C/parallel ",
    "CS" : "../C/serial ",
    "Kotlin" : "../Kotlin/gradlew -p ../Kotlin/ run --args "
}

filetoUse = {
    "Python" : "../Results/Python_results.csv",
    "CP" : "../Results/C_Parallel_results.csv",
    "CS" : "../Results/C_Serial_results.csv",
    "Kotlin" : "../Results/Kotlin_results.csv"
}

if ( "--no-python" in sys.argv):
    languageToUse.pop("Python")
    filetoUse.pop("Python")

def cleanup():
    os.system("rm ../Results/*.csv")
def runprog(language):
    for i in data_range:
        os.system(languageToUse[language] + str(i) + " > /dev/null")

def initialiseDict(language):
   
    fileUsing = open(filetoUse[language], "r")
    csv_reader = csv.reader(fileUsing, delimiter=",")
    for row in csv_reader:
        bigDict[row[1]] = []
    languagesdict[language] = {}
        
def averageResults(language, landict):
    fileUsing = open(filetoUse[language], "r")
    csv_reader = csv.reader(fileUsing, delimiter=",")
    for row in csv_reader:
        if row[1] in landict:
            bigDict[row[1]].append(float(row[2])) 
   
    for key in landict:
        languagesdict[language][key] = numpy.average(landict[key])

    
    


def sendTofinalResults(dictToUse):

    filename = "../Results/results.csv"
    
    header = "size,"
    for key in filetoUse:
            header += key + ','
    header += "\n"

    fileContent = header
    for size in data_range:
        contents = "{},".format(size)
        for key in filetoUse:
            contents += str(dictToUse[key][str(size)]) + ','
        
        contents += "\n"
        fileContent += contents

    f = open(filename, "w+")
    f.write(fileContent)
    f.close()




cleanup()


for language in languageToUse:
    
    for run in range(num_runs):
        runprog(language)

    initialiseDict(language)
    averageResults(language,bigDict)
    bigDict.clear()


sendTofinalResults(languagesdict)


