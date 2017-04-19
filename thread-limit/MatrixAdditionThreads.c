#include <stdio.h>
#include <omp.h>
#include <stdlib.h>
#include <time.h>
#define DIMENSION 10000
void main()
{
    int *matrixA[DIMENSION];
    int *matrixB[DIMENSION];
    int *matrixC[DIMENSION];
    int i, j;
    int N;
    double t;
    
    //Initialising 2 D array on the heap
    for (i=0; i<DIMENSION; i++)
    {
         matrixA[i] = (int *)malloc(DIMENSION * sizeof(int));
         matrixB[i] = (int *)malloc(DIMENSION * sizeof(int));
         matrixC[i] = (int *)malloc(DIMENSION * sizeof(int));
    }
    
    
    srand(time(NULL));
    //Initialises the elements of the array
    //Here, if we use openmp, it increases the time. That is because of the rand() function
    //It is not thread safe.
    for(i = 0; i<DIMENSION; i++)
            matrixA[i][j] = rand();
            
    for(i = 0; i<DIMENSION; i++)
        matrixB[i][j] = rand();  
          
    //To calculate the time the function takes
    t = omp_get_wtime();
//Does addition parallely
#pragma omp parallel for 
for(int i=0;i<DIMENSION;i++) 
{
    for(int j=0;j<DIMENSION;j++) {
        N = omp_get_num_threads();
        matrixC[i][j]=matrixA[i][j]+matrixB[i][j];
        }   
}
    printf( "time = %f\n", omp_get_wtime()-t );

    printf("The number of threads launched are %d\n",N);          
           
}
