import java.util.LinkedList;

public class Queue<T> {
    private LinkedList<T> Queue;

    public Queue() {
        this.Queue = new LinkedList<T>();
    }

    public void enqueue(T e) {
        Queue.add(e);
    }

    public T dequeue() {
        return(Queue.pollFirst());
    }

    public T peek() {
        return(Queue.peek());
    }

    public boolean isEmpty() {
        return(Queue.size() == 0);
    }

    public int isSize(){
        return Queue.size();
    }


}
