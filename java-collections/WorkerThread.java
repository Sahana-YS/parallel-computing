import java.util.*;
public class WorkerThread implements Runnable {
  private List<String> list = null;

  public WorkerThread(List<String> l) {
    list = l;
  }

  @Override public void run() {
    for(int i = 0; i < 10000; ++i) {
      Integer rand1 = (int) Math.ceil(Math.random() * 1000000);
      Integer rand2 = (int) Math.ceil(Math.random() * 1000000);

      Integer getIndex = list.indexOf(String.valueOf(rand1));
      list.add(String.valueOf(rand2));
    }
  }
}
