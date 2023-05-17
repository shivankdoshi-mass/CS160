import static org.junit.Assert.assertEquals;
import org.junit.Test;


public class CarTests {

    public static void main(String[] args){
    }

    @Test
    public void ConstructorTest(){
        Car car = new Car(0, 0, 0);
        assertEquals(0,car.getPowerSource());
    }
    
    @Test
    public void getIdTest(){
        Car car = new Car(1, 0, 0);
        assertEquals(1, car.getId());
    }
    
    @Test
    public void setIDTest(){
        Car car = new Car(1, 2, 5);
        car.setId(2);
        assertEquals(2, car.getId());
    }


    @Test
    public void getPowerSourceTest(){
        Car car = new Car(0, 0, 0);
        assertEquals(0, car.getPowerSource());
    }

    @Test
    public void setPowerSourceTest(){
        Car car = new Car(1, 2, 5);
        car.setId(1);
        assertEquals(1, car.getId());
    }
    
    @Test
    public void getPricePerDayTest(){
        Car car = new Car(0, 0, 5);
        assertEquals(5, car.getPricePerDay(), 0);
    }

    @Test
    public void setPricePerDayTest(){
        Car car = new Car(1, 2, 5);
        car.setPricePerDay(5);
        assertEquals(5, car.getPricePerDay(), 0);
    }

}
