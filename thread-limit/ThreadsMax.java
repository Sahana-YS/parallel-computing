//Example to demonstrate maximum number of threads in java 
//Main class
public class ThreadsMax {
    public static void main(String[] argv){
        //Infinite loop - Creates threads and calls the run method of the thread class
        for(;;){
            new Thread(new Worker()).start();
        }
    }
}

class Worker extends Thread
{
    private static Object s = new Object();
    private static int count = 0;
    public void run()
    {
        //When a thread executes the below statement, it acquires a lock on object s and unitil it releases the 
        //lock, another thread cannot lock the object and the first thread releases the lock only after it 
        //finishes executing the block which follows it. 
        synchronized(s){
           count += 1;
           System.err.println("New thread #"+count);
        }
        for(;;){
           try {
              Thread.sleep(1000);
           } catch (Exception e){
              System.err.println(e);
           }
        }
    }
}
