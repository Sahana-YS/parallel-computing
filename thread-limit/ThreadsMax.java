public class ThreadsMax {
    private static Object s = new Object();
    private static int count = 0;
    public static void main(String[] argv){
        for(;;){
            new Thread(new Runnable(){
                    public void run(){
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
                }).start();
        }
    }
}
