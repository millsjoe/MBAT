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
    
# which programs to use
languageToUse = {
    "Python" : "python3 ../Python/Numpy_plotting.py ",
    "CP" : "../C/parallel ",
    "CS" : "../C/serial ",
    "Kotlin" : "../Kotlin/gradlew -p ../Kotlin/ run --args "
}

# which performance results to use
filetoUse = {
    "Python" : "../Results/Python_results.csv",
    "CP" : "../Results/C_Parallel_results.csv",
    "CS" : "../Results/C_Serial_results.csv",
    "Kotlin" : "../Results/Kotlin_results.csv"
}

# allow no-python option for optimum speed
if ( "--no-python" in sys.argv):
    languageToUse.pop("Python")
    filetoUse.pop("Python")

# cleanup csv files before beginning
def cleanup():
    os.system("rm ../Results/*.csv")

# run each script required
def runprog(language):
    for i in data_range:
        os.system(languageToUse[language] + str(i) + " > /dev/null")

# initialise the final language dict
def initialiseDict(language):
   
    fileUsing = open(filetoUse[language], "r")
    csv_reader = csv.reader(fileUsing, delimiter=",")
    for row in csv_reader:
        bigDict[row[1]] = []
    languagesdict[language] = {}

#  calculate the average for each language and add it to dict        
def averageResults(language, landict):
    fileUsing = open(filetoUse[language], "r")
    csv_reader = csv.reader(fileUsing, delimiter=",")
    for row in csv_reader:
        if row[1] in landict:
            bigDict[row[1]].append(float(row[2])) 
   
    for key in landict:
        languagesdict[language][key] = numpy.average(landict[key])

    
    

# output dict contents to csv file
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

# call on all functions to run 
for language in languageToUse:
    
    for run in range(num_runs):
        runprog(language)

    initialiseDict(language)
    averageResults(language,bigDict)
    bigDict.clear()


sendTofinalResults(languagesdict)


