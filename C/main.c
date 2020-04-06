#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
int SIZE;
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
void initialiseStartingCell( int arrayBoard[SIZE][SIZE]){
    float middle = SIZE/2;
    int startingPoint = (int)middle - 1 ;

    arrayBoard[startingPoint][startingPoint] = 1;
}
int main(int argc, char* argv[]) {

    SIZE = atoi(argv[1]); // take user input convert to int
    int count = atoi(argv[2]);

    int (*arrayBoard)[SIZE];
    arrayBoard = malloc(sizeof(int[SIZE][SIZE]));
    memset(arrayBoard, 0, SIZE * SIZE); // create an array initialise with zeros
//    checkArray(arrayBoard);
    createBorder(arrayBoard);
    return 0;
}