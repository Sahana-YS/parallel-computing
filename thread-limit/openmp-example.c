#include <stdlib.h>
#include <stdio.h>
#include <omp.h>
#define N 1000
int main()
{
    int i, *a;
    int sum = 0;
    double t;
    a = (int*)malloc(N*sizeof(int));
    t = omp_get_wtime();
    //Parallel sections - The initialization and finding sum is done in parallel
   #pragma omp parallel shared(a, sum)
   {
    #pragma omp for
   for( i=0; i<N; ++i)
    { 
       a[i] = i; 
    }
    #pragma omp for reduction(+:sum)
   for( i=0; i<N; ++i)
    {
        sum += a[i]; 
    }
  }
    //Prints the sum and the time taken in the parallel section
    printf( "sum =%d, t = %f\n", sum, omp_get_wtime()-t );
    return 0;
}
