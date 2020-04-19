#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <time.h>
#include <zconf.h>
#include <math.h>


int SIZE;

void appendResults(float time){
    FILE *fp;
    fp = fopen("../Results/C_Serial_results.csv", "a+");
    fprintf(fp,"CS,%d,%.5f\n",SIZE,time);

}

void printArray(int arrayBoard[SIZE][SIZE]){

    int number = SIZE;
    int digits = 0;
    while (number > 0) {
        number = number/10;
        digits++;
    }

    FILE *fp;
    char* location = "../JSON/";
    char* name = "CS_"; 
    char* extension = ".json";
    char filetouse[strlen(location)+strlen(name)+strlen(extension)+digits+1];

    snprintf( filetouse, sizeof( filetouse ), "%s%s%d%s", location, name, SIZE, extension );
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

void createBorder(int arrayBoard[SIZE][SIZE]){


    for (int i = 0; i < SIZE; i++){
        arrayBoard[0][i] = 2;
        arrayBoard[i][0] = 2;
        arrayBoard[SIZE- 1][i] = 2;
        arrayBoard[i][SIZE -1]= 2;
    }

}

int genNum(){
    return (rand() % (SIZE-2) - 2 + 1 ) + 2; // minus 2 to allow for the border
}

void initialiseStartingCell( int arrayBoard[SIZE][SIZE]){
    float middle = SIZE/2;
    int startingPoint = (int)middle - 1 ;

    arrayBoard[startingPoint][startingPoint] = 1;
}

bool diffuse(int x, int y, int arrayBoard[SIZE][SIZE], int count ){
        if (count > 50000){
            return false;
        }
        if (checkDiffused(arrayBoard,x,y)){
            arrayBoard[x][y] = 1;
            return true;
        }
        if (checkBorder(arrayBoard,x,y)){
            x = genNum();
            y = genNum();
        }
        else{
            int decider = (rand() % 4 - 1 + 1) + 1;

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
    int count = (SIZE*0.4) * (SIZE*0.1);

    clock_t begin = clock();
    int (*arrayBoard)[SIZE];
    arrayBoard = malloc(sizeof(int[SIZE][SIZE]));
    memset(arrayBoard, 0, SIZE * SIZE); // create an array initialise with zeros


//    checkArray(arrayBoard);
    createBorder(arrayBoard);


    int x,y;

    srand(time(NULL)); // has to be here for genuine randomness

    x = genNum();
    y = genNum();

    initialiseStartingCell(arrayBoard);
    int i = 0;
    while(i < count){
        if (diffuse(x, y, arrayBoard,0)){
            i++;
        }
    }

    clock_t end = clock();
    double time_spent = (double)(end - begin) / CLOCKS_PER_SEC;

    printArray(arrayBoard);
    appendResults(time_spent);

    free(arrayBoard);

    return 0;
}