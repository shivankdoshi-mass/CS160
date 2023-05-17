import static org.junit.Assert.assertEquals;
import java.util.LinkedList;
import org.junit.Test;

public class CarFleetTests {    
    public static void main(String[] args){
        
    }

    @Test
    public void ConstructorTest(){
        CarFleet car = new CarFleet();
        assertEquals(true, car.electricCars.isEmpty());
    }

    @Test
    public void addCarTest(){
        CarFleet car = new CarFleet();
        car.addCar(new Car(1, 1, 1));
        assertEquals(false, car.gasCars.isEmpty());  
        assertEquals(true, car.electricCars.isEmpty());     
    }

    @Test
    public void processRequestsTest(){
        
        Queue <Integer> QueueofTypeCar = new Queue<Integer>();
        QueueofTypeCar.enqueue(1);
        QueueofTypeCar.enqueue(2);
        QueueofTypeCar.enqueue(3);

        CarFleet car = new CarFleet();
        LinkedList <Car> listofcars = car.processRequests(QueueofTypeCar);

        Car poppedfirst = listofcars.pollFirst();
        assertEquals(1, poppedfirst.getPowerSource());   
        
        poppedfirst = listofcars.pollFirst();
        assertEquals(2, poppedfirst.getPowerSource());   

        poppedfirst = listofcars.pollFirst();
        assertEquals(3, poppedfirst.getPowerSource());   




    }

}
