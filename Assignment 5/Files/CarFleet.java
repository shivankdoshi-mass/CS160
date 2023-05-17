import java.util.LinkedList;

public class CarFleet{    
    public Queue<Car> gasCars;
    public Queue<Car> hybridCars;
    public Queue<Car> electricCars;

    CarFleet() {
        this.gasCars = new Queue<Car>();
        this.hybridCars = new Queue<Car>();
        this.electricCars = new Queue<Car>();
    }

    public boolean addCar(Car car){
        int powerSource = car.getPowerSource();
        if (powerSource == 1){
            this.gasCars.enqueue(car);
            return true;
        }

        else if (powerSource == 2){
            this.hybridCars.enqueue(car);
            return true;
        }
        else if (powerSource == 3){
            this.electricCars.enqueue(car);
            return true;
        }
        return false;
    }

    public LinkedList <Car> processRequests(Queue <Integer> listofCartype){    
        int sizeofcartype = listofCartype.isSize();   
        LinkedList <Car> carArrayList = new LinkedList <Car>();
        for (int i = 0; i < sizeofcartype; i++) {
            int dequeue = listofCartype.dequeue() ;
            if (dequeue == 1){
                Car newcar = new Car(0,1,0);
                carArrayList.add(newcar);
            }
            else if (dequeue == 2){
                Car newcar = new Car(0,2,0);
                carArrayList.add(newcar);
            }
            else if (dequeue == 3){
                Car newcar = new Car(0,3,0);
                carArrayList.add(newcar);
            }
          }
  
        return carArrayList;
    }

}

