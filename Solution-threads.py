import random
import time
import threading
NArray = [16, 64, 256, 512, 1024, 2048, 4096 ]
#Writes to a file
f = open('brute-force-4-threads','w')
#declares 2 dimensional arrays
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
        #Generate matrix 1 with random numbers
        for x in range(0,N):
            for y in range(0,N):
                randomNo = round(random.uniform(0,100),2)
                matrix1[x][y] = randomNo

        #Generate matrix 2 with random numbers
        for x in range(0,N):
            for y in range(0,N):
                randomNo = round(random.uniform(0,100),2)
                matrix2[x][y] = randomNo

    # Computes the result serially
    def innerProduct():
        for i in range(0,N):
            for j in range(0,N):
                for k in range(0,N):
                    matrix3[i][j] = matrix3[i][j]+ matrix1[i][k]*matrix2[k][j]

    # Computing the result parallelly. This function is the function which is called by each thread launched.
    def calculateResult(a,b):
        for i in range(a,b):
            for j in range(0,N):
                for k in range(0,N):
                    matrix4[i][j] = matrix4[i][j]+ matrix1[i][k]*matrix2[k][j]

    # Creates 4 threads and work is split across each thread, each thread calls calculateResult
    def innerProductParallel():
        try:
            #4 threads
            t1=threading.Thread(target=calculateResult,args=(0,N/4,))
            t1.daemon = True
            t1.start()
            t2=threading.Thread(target=calculateResult,args=(N/4,N/2,))
            t2.daemon = True
            t2.start()
            t3=threading.Thread(target=calculateResult,args=(N/2,(3*N)/4,))
            t3.daemon = True
            t3.start()
            t4=threading.Thread(target=calculateResult,args=((3*N)/4,N,))
            t4.daemon = True
            t4.start()

            t1.join()
            t2.join()
            t3.join()
            t4.join()
        except:
            print "Error: unable to start thread"

    #generates the matrix
    generateMatrix()
    #time taken for serial matrix multiplication
    t0 = int(round(time.time() * 1000))
    innerProduct()
    t1 = int(round(time.time() * 1000))
    T3 = t1 - t0
    #prints the statistics to the file and on the console
    print "%d elements" %(N)
    f.write("%d elements\n" %(N))
    print "Inner product method"
    f.write("Inner product method\n")
    print "The time taken for multiplication is %d milliseconds" %(T3)
    f.write("The time taken for multiplication is %d milliseconds\n" %(T3))
    print "\n"
    f.write('\n')
    #time taken for matrix multiplication using threads
    t2 = int(round(time.time() * 1000))
    innerProductParallel()
    t3 = int(round(time.time() * 1000))
    T4 = t3 - t2
    #prints the statistics onto the console and into the file
    print "%d elements" %(N)
    f.write("%d elements\n" %(N))
    print "Inner product method with threads"
    f.write("Inner product method with threads\n")
    print "The time taken for multiplication is %d milliseconds" %(T4)
    f.write("The time taken for multiplication is %d milliseconds\n" %(T4))
    #prints the last element to see if the computation is proper
    print matrix3[N-1][N-1]
    print matrix4[N-1][N-1]
    print "\n"
    f.write('\n')
