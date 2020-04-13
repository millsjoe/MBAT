import os 
import numpy
import sys

language = str(sys.argv[1])
start = int(sys.argv[2])
end = int(sys.argv[3])
increment = int(sys.argv[4])
data_range = numpy.arange(start,end,increment)


languageToUse = {
    "Python" : "python3 ../Python/Numpy_plotting.py ",
    "C" : "../C/parallel ",
    "Kotlin" : "../Kotlin/gradlew run --args "
}

for i in data_range:
    os.system(languageToUse[language] + str(i))
    