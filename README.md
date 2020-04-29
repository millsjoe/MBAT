# MBAT
Final year project: Modelling Bacteria &amp; Tumours

3 Applications are available to run which generate JSON files to model Diffusion-Limited Aggregration (DLA). These applications are developed in Python, Kotlin & C. A serial and parallel version are available in C. 

The output of all applications is a JSON file in `../JSON/` and a CSV of results in `../Results`
## Python 
### Dependencies
In order to run in Python you must have Python 3.6+, pip3 and the relevant pip modules. `requirements.txt` contains the modules required and can be installed by:
```
$ pip3 install -r requirements.txt
```
### Application
To run the DLA use the following command:
```
$ python3 Numpy_plotting.py {environment_size}
e.g $ python3 Numpy_plotting.py 100
```
## Kotlin
### Dependencies 
First Kotlin must be installed on the system. For MacOS use homebrew:
```
$ brew install kotlin
```
For Linux installations (Ubuntu) please follow the following [guide](https://linuxhint.com/kotlin_ubuntu/)
To verify installtion run `kotlinc` to view the Kotlin shell.
### Application
A gradle build is used and can be run:
```
$ ./gradlew run --args {environment_size}
e.g $ ./gradlew run --args 100
```

## C
### Serial
The serial application is compiled using `gcc`:
```
$ gcc serial.c -o serial
``` 
And is ran:
```
$ ./serial {environment_size}
e.g $ ./serial 100
```
### Parallel 
The parallel application is comipled with `gcc` and `OpenMP`:
```
gcc -fopenmp parallel.c -o parallel
```
And is ran:
```
$ ./parallel {environment_size}
e.g $ ./parallel 100
```
## Visualising
### Models
To visualise the models use the Python script `generateModel.py`. The following syntax will generate a model:
```
$ python3 generateModel.py --model {language} {environment_size}
e.g $ python3 generateModel.py --model Kotlin 100
```
For C applications, the language argument for parallel is `CP` and for serial `CS`.
All models are saved in the relevant image directory for the language i.e `Python/Python_images/`
### Fractal dimension
To determine the fractal dimension. A series of models must be generated first in an appropriate range. The range must have a suitable increment too i.e 10-100 with increments of 10. To caclulate the fractal dimension use:
```
$ python3 generateModel.py --fractal {language} {range_start} {range_end} {increment}
e.g $ python3 generateModel.py --fractal CP 10 100 10
```
The fractal dimension will be displayed onscreen and have the ability to save if required.

## Results Gather 
In order to retreive the average results of all langauges, a script is available to run all languages. NOTE C applications must be compiled previous to running this script. The script runs using:
```
$ python3 run_results.py {range_start} {range_end} {increment} {num_runs}
e.g $ python3 run_results.py 10 100 10 5 
```
The average results can be found `./Results/results.csv` in format `size,python,cp,cs,kotlin`
