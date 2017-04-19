Running the openmp-example.c,
$ gcc -fopenmp -o openmp-example.c
$ env OMP_NUM_THREADS=<Number of threads> ./openmp-example

Running the MatrixAdditionThreads.c,
$ gcc -fopenmp -o MatrixAdditionThreads.c
$ env OMP_NUM_THREADS=<Number of threads> ./MatrixAdditionThreads


Running ThreadsMax.java
$ javac ThreadsMax.java
$ java ThreadsMax
