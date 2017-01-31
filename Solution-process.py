import random
import time
import threading
from multiprocessing import Process,Manager
NArray = [16, 64, 256, 512, 1024, 2048, 4096 ]
# Writes to a file
f = open('brute-force-4-processes','w')
for N in NArray:
    matrix1 = [[0 for x in range(0,N)] for y in range(0,N)]
    matrix2 = [[0 for x in range(0,N)] for y in range(0,N)]
    matrix3 = [[0 for x in range(0,N)] for y in range(0,N)]
    matrix4 = [[0 for x in range(0,N)] for y in range(0,N)]
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

    # Serial matrix multiplication
    def innerProduct():
        for i in range(0,N):
            for j in range(0,N):
                for k in range(0,N):
                    matrix3[i][j] = matrix3[i][j]+ matrix1[i][k]*matrix2[k][j]

    #Parallel matrix multiplication
    def calculateResult(a,b,matrix4):
        for i in range(a,b):
            for j in range(0,N):
                for k in range(0,N):
                    matrix4[i][j] = matrix4[i][j]+ matrix1[i][k]*matrix2[k][j]

    # Creates 4 processes and work is split across each process, each process calls calculateResult.
    # But since the processes donot share the memory by default each process updates its own local variable
    # and at the end after all the processes join, the changes made by each of the process is not updated in
    # the global variable.
    def innerProductParallel():
        try:
            # 4 Processes
            t1=Process(target=calculateResult,args=(0,N/4,matrix4,))
            t2=Process(target=calculateResult,args=(N/4,N/2,matrix4,))
            t3=Process(target=calculateResult,args=(N/2,(3*N)/4,matrix4,))
            t4=Process(target=calculateResult,args=((3*N)/4,N,matrix4,))
            t1.start()
            t2.start()
            t3.start()
            t4.start()
            t1.join()
            t2.join()
            t3.join()
            t4.join()
        except:
            print "Error: unable to start thread"

    generateMatrix()
    t0 = int(round(time.time() * 1000))
    innerProduct()
    t1 = int(round(time.time() * 1000))
    T3 = t1 - t0
    print "%d elements" %(N)
    f.write("%d elements\n" %(N))
    print "Inner product method"
    f.write("Inner product method\n")
    print "The time taken for multiplication is %d milliseconds" %(T3)
    f.write("The time taken for multiplication is %d milliseconds\n" %(T3))
    print "\n"
    f.write('\n')

    t6 = int(round(time.time() * 1000))
    innerProductParallel()
    t7 = int(round(time.time() * 1000))
    T6 = t7 - t6
    print "Inner product method with processes"
    f.write("Inner product method with processes\n")
    print "The time taken for multiplication is %d milliseconds" %(T6)
    f.write("The time taken for multiplication is %d milliseconds\n" %(T6))
    print "\n"
    f.write('\n')
