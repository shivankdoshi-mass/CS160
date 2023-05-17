import static org.junit.Assert.assertEquals;
import org.junit.Test;

public class QueueTests {    
    public static void main(String[] args){
    }

    @Test 
    public void genericTest(){
        Queue <String> testString = new Queue <String>();
        Queue <Integer> testInt = new Queue <Integer>();
        testString.enqueue("String");
        testInt.enqueue(0);
        assertEquals(true, testString.dequeue() instanceof String);
        assertEquals(true, testInt.dequeue() instanceof Integer);
    }

    @Test
    public void ConstructorTest(){
        Queue <String> tests = new Queue <String>();
        assertEquals(true, tests.isEmpty());
    }

    @Test
    public void EnqueueTest(){
        Queue <String> tests = new Queue <String>();
        tests.enqueue("honda");
        assertEquals("honda", tests.peek());
    }
 
    @Test
    public void DequeueTest(){
        Queue <String> tests = new Queue <String>();
        tests.enqueue("honda");    
        tests.dequeue();
        assertEquals(true, tests.isEmpty());
    }

    @Test
    public void peekTest(){
        Queue <String> tests = new Queue <String>();
        tests.enqueue("honda");
        assertEquals("honda", tests.peek());

    }

    @Test
    public void isEmptyTest(){
    Queue <String> tests = new Queue <String>();
    assertEquals(true, tests.isEmpty());
    }    
    }

