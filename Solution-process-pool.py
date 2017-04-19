import random
import time
import threading
from multiprocessing import Pool
NArray = [16, 64, 256, 512, 1024, 2048, 4096  ]
# Writing to a file
f = open('brute-force-4-processes-pool','w')
for N in NArray:
    #initialises the matrices
    matrix1 = [[0 for x in range(0,N)] for y in range(0,N)]
    matrix2 = [[0 for x in range(0,N)] for y in range(0,N)]
    matrix3 = [[0 for x in range(0,N)] for y in range(0,N)]
    resultMatrix = [[0 for x in range(0,N)] for y in range(0,N)]
    M1 = [[0 for x in range(0,N)] for y in range(0,N)]
    M2 = [[0 for x in range(0,N)] for y in range(0,N)]
    M01 = [[0 for x in range(0,N)] for y in range(0,N)]
    M02 = [[0 for x in range(0,N)] for y in range(0,N)]
    def generateMatrix():
        #Generate matrix 1
        for x in range(0,N):
            for y in range(0,N):
                randomNo = round(random.uniform(0,100),2)
                matrix1[x][y] = randomNo

        #Generate matrix 2
        for x in range(0,N):
            for y in range(0,N):
                randomNo = round(random.uniform(0,100),2)
                matrix2[x][y] = randomNo

    # Matrix multiplication in serial
    def innerProduct():
        for i in range(0,N):
            for j in range(0,N):
                for k in range(0,N):
                    matrix3[i][j] = matrix3[i][j]+ matrix1[i][k]*matrix2[k][j]

    # Each process does its part of the work in the whole matrix and returns the resultant matrix which it computes
    def calculateResult(args):
        a = args[0]
        b = args[1]
        matrix = [[0 for x in range(0,N)] for y in range(0,N)]
        for i in range(a,b):
            for j in range(0,N):
                for k in range(0,N):
                    matrix[i][j] = matrix[i][j]+ matrix1[i][k]*matrix2[k][j]
        return matrix

    # After all the processes complete the task, the changes made by each of the process has to be combined
    # to get the final answer
    def combine(matrix):
        resMatrix = []
        for j in range(0,N/4):
            resMatrix.append(matrix[0][j])
        for j in range(N/4,N/2):
            resMatrix.append(matrix[1][j])
        for j in range(N/2,(3*N)/4):
            resMatrix.append(matrix[2][j])
        for j in range((3*N)/4,N):
            resMatrix.append(matrix[3][j])
        return resMatrix

    # Creates 4 processes and work is split across each process, each process calls calculateResult.
    def innerProductParallel():
        resultMatrix = []
        try:
            # Creates a pool of processes
            p = Pool(processes = 4)
            # Array of arguments that have to be passed to each of the process's calculateResult
            args = [[0,N/4],[N/4,N/2],[N/2,(3*N)/4],[(3*N)/4,N]]
            # matrix4 will have the matrices(return value of calculateResult) returned by each of the process
            matrix4 = p.map(calculateResult,args)
            # combine is called to combine the results computed by all the processes
            resultMatrix = combine(matrix4)
        except:
            print "Error: unable to start thread"
        return resultMatrix

    #generates the matrix
    generateMatrix()
    #time taken by the brute force approach
    t0 = int(round(time.time() * 1000))
    innerProduct()
    t1 = int(round(time.time() * 1000))
    T3 = t1 - t0
    #writes the result into the file and prints it on the console
    print "%d elements" %(N)
    f.write("%d elements\n" %(N))
    print "Inner product method"
    f.write("Inner product method\n")
    print "The time taken for multiplication is %d milliseconds" %(T3)
    f.write("The time taken for multiplication is %d milliseconds\n" %(T3))
    print "\n"
    f.write('\n')

    #time taken by the parallel method
    t6 = int(round(time.time() * 1000))
    res = innerProductParallel()
    t7 = int(round(time.time() * 1000))
    T6 = t7 - t6
    #writes the result onto the console and into the file
    print "Inner product method with processes"
    f.write("Inner product method with processes\n")
    print "The time taken for multiplication is %d milliseconds" %(T6)
    f.write("The time taken for multiplication is %d milliseconds\n" %(T6))
    print matrix3[N-1][N-1]
    print res[N-1][N-1]
    print "\n"
    f.write('\n')
