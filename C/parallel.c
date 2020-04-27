#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <time.h>
#include <zconf.h>
#include <omp.h>
#include <math.h>


int SIZE;

// Print results to csv file
void appendResults(float time){
    FILE *fp;
    fp = fopen("../Results/C_Parallel_results.csv", "a+");
    fprintf(fp,"CP,%d,%.5f\n",SIZE,time);

}

// Output matrix to json file
void printArray(int arrayBoard[SIZE][SIZE]){

    int number = SIZE;
    int digits = 0;
    while (number > 0) {
        number = number/10;
        digits++;
    }

    FILE *fp;
    char* location = "../JSON/";
    char* name = "CP_"; 
    char* extension = ".json";
    char filetouse[strlen(location)+strlen(name)+strlen(extension)+digits+1];

    snprintf( filetouse, sizeof( filetouse ), "%s%s%d%s", location, name, SIZE, extension ); // Allows dynamic file naming
    fp = fopen(filetouse, "w+");


    fprintf(fp,"{\n\"modelArray\" : [\n");
    for (int i = 0; i <SIZE; i ++) {
        fprintf(fp,"[");
        for (int j = 0; j < SIZE; j++) {
            if (j == SIZE -1){
                fprintf(fp,"%d", arrayBoard[i][j]);
            }
            else{
                fprintf(fp,"%d,", arrayBoard[i][j]);
            }


        }
        if (i == SIZE -1){
            fprintf(fp,"]\n");
        }
        else{
            fprintf(fp,"],\n");
        }
    }
    fprintf(fp,"]\n}");
    fclose(fp);
}

// Used for debugging purposes and small arrays
// Prints the entire array
void checkArray(int arrayBoard[SIZE][SIZE]) {
    for (int i = 0; i < SIZE; i++) {
        printf("[");
        for (int j = 0; j < SIZE; j++) {
            if (j == SIZE - 1) {
                printf("%d", arrayBoard[i][j]);
            } else {
                printf("%d,", arrayBoard[i][j]);
            }


        }
        if (i == SIZE - 1) {
            printf("]\n");
        } else {
            printf("],\n");
        }
    }
}

// Detemrine if too close to border or on an already diffused cell
bool checkBorder(int arrayBoard[SIZE][SIZE], int locationX, int locationY){

    bool toReturn = false;
    if (arrayBoard[locationX][locationY + 1] == 2 ||
        arrayBoard[locationX][locationY - 1] == 2 ||
        arrayBoard[locationX + 1][locationY] == 2 ||
        arrayBoard[locationX - 1][locationY] == 2){
        toReturn = true;
    }
    if(arrayBoard[locationX][locationY] == 1)
        toReturn = true;

    return toReturn;
}

// Check if cell has completed diffusion
bool checkDiffused(int arrayBoard[SIZE][SIZE], int locationX, int locationY){

    bool toReturn = false;
    if (arrayBoard[locationX][locationY + 1] == 1 ||
        arrayBoard[locationX][locationY - 1] == 1 ||
        arrayBoard[locationX + 1][locationY] == 1 ||
        arrayBoard[locationX - 1][locationY] == 1){
        toReturn = true;
    }

    return toReturn;
}

// Create border of cell
void createBorder(int arrayBoard[SIZE][SIZE]){


    for (int i = 0; i < SIZE; i++){
        arrayBoard[0][i] = 2;
        arrayBoard[i][0] = 2;
        arrayBoard[SIZE- 1][i] = 2;
        arrayBoard[i][SIZE -1]= 2;
    }

}
 // Generate a pseudo-random number
int genNum(){
    return (rand() % (SIZE-2) - 2 + 1 ) + 2; // minus 2 to allow for the border
}

// Place first cell in the middle
void initialiseStartingCell( int arrayBoard[SIZE][SIZE]){
    float middle = SIZE/2;
    int startingPoint = (int)middle - 1 ;

    arrayBoard[startingPoint][startingPoint] = 1;
}
 // Diffuse in a recursive matter. Will return if exceeding the recursion counter
bool diffuse(int x, int y, int arrayBoard[SIZE][SIZE], int count ){

        // Recursion counter
        if (count > 4000){
            return false;
        }
        if (checkDiffused(arrayBoard,x,y)){
            // Only allow one thread to make changes on shared memory
            #pragma omp critical 
            {
                arrayBoard[x][y] = 1;
            }
            return true;
        }

        if (checkBorder(arrayBoard,x,y)){
            x = genNum();
            y = genNum();
        }
        else{
            int decider = (rand() % 4 - 1 + 1) + 1;
            // Move to next random location
            switch(decider){
                case 1 :
                    x = x - 1;
                    y = y;
                    break;
                case 2 :
                    x = x + 1;
                    y = y;
                    break;
                case 3 :
                    x = x;
                    y = y - 1;
                    break;
                case 4 :
                    x = x;
                    y = y + 1;
                    break;
            }
        }
        count++;
        diffuse(x, y, arrayBoard, count);

    }

int main(int argc, char* argv[]) {

    SIZE = atoi(argv[1]); // take user input convert to int
    int count = (SIZE*0.2) * (SIZE*0.2);
    int (*arrayBoard)[SIZE];

    double begin = omp_get_wtime();

    arrayBoard = malloc(sizeof(int[SIZE][SIZE]));
    memset(arrayBoard, 0, SIZE * SIZE); // create an array initialise with zeros


    createBorder(arrayBoard);


    int x,y;

    srand(time(NULL)); // has to be here for genuine randomness

    

    initialiseStartingCell(arrayBoard);
    int tid;
    #pragma omp parallel for private(x, y, tid) // diffuse in parallel with private locations per thread
    for (int i = 0; i < count; i++){

        tid = omp_get_thread_num();
        x = genNum();
        y = genNum();
        if (!diffuse(x,y,arrayBoard,0))
            i = i-1;
    //    printf("x: %d y: %d thread: %d \n", x,y,tid); // This checks to see if the multithreading works as expected 
    }

    double time_spent = omp_get_wtime() - begin;
    // printf("%f\n", time_spent);

    printArray(arrayBoard);
    appendResults(time_spent);
    free(arrayBoard);

    return 0;
}