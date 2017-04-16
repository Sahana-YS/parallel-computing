#include <stdlib.h>
#include <stdio.h>
#include <omp.h>
#define N 1000
int main()
{
    int i, *a;
    long long sum = 0;
    double t;
    a = (int*)malloc(N*sizeof(int));
    t = omp_get_wtime();
#pragma omp parallel shared( a, sum )
    {
#pragma omp for
   for( i=0; i<N; ++i)
       { a[i] = i; }
#pragma omp for reduction(+:sum)
   for( i=0; i<N; ++i)
       { sum += a[i]; }
    }
    printf( "sum =%lld, t = %f\n", sum, omp_get_wtime()-t );
    return 0;
}
