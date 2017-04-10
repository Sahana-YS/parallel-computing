import java.util.Collections;
import java.util.*;
import java.util.ArrayList;
import java.util.concurrent.CopyOnWriteArrayList;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class MainProgram {
  private static final int NUMTHREADS = 3;
  private static final int NUMITER = 20;

  public static void main(String[] args) {
    System.out.println("Starting");
    int listType = Integer.parseInt(args[0]);

    for(int i = 0; i < NUMITER; ++i) {
      List<String> list = null;
      switch(listType) {
        case 0: list = new ArrayList<String>(); break;
        case 1: list = Collections.synchronizedList(new ArrayList<String>()); break;
        case 2: list = new CopyOnWriteArrayList<String>(); break;
      }

      long start = System.currentTimeMillis();
      ExecutorService executor = Executors.newFixedThreadPool(NUMTHREADS);
      for(int j = 0; j < NUMTHREADS; ++j) {
        executor.execute(new WorkerThread(list));              
      }
      executor.shutdown();
      while (!executor.isTerminated())
        ;
      if(listType == 0)
      	System.out.println("ArrayList," + (System.currentTimeMillis() - start));
      if(listType == 1)
      	System.out.println("Synchronized list," + (System.currentTimeMillis() - start));
      if(listType == 2)
      	System.out.println("Copy on write ArrayList," + (System.currentTimeMillis() - start));
    }
  }
}
