#include <iostream>
#include <cstring>
#include <omp.h>

using namespace std;

int main()
{
int A[100000], i;
clock_t tic, toc;
 
tic = clock();
 //Normal way of initialising
for (int j=0; j<10000; j++) for (i=0; i<100000; i++) A[i]=j;
toc = clock();
cout << "Without memset:"<< (toc-tic)*1.0/CLOCKS_PER_SEC << endl;

tic = clock();
 //Using memset to initialise
for (int j=0; j<10000; j++) memset(A, j, sizeof(A));
toc = clock();
cout << "With memset:"<<(toc-tic)*1.0/CLOCKS_PER_SEC << endl;

return 0;
}

/**
sahana@Sahana-Inspiron-3543:~/VI Semester/Parallel Computing/Blog/Post 2$ g++ memset.cpp 
sahana@Sahana-Inspiron-3543:~/VI Semester/Parallel Computing/Blog/Post 2$ ./a.out 
Without memset:2.70535
With memset:0.157259
**/
