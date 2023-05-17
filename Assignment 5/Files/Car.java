public class Car {
    private int id;
    private int powerSource;
    private float pricePerDay;
    
    Car(int id, int powerSource, float pricePerDar) {
        this.id = id;
        this.powerSource = powerSource;
        this.pricePerDay = pricePerDar;
    }

    public int getId() {
        return this.id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public int getPowerSource() {
        return this.powerSource;
    }

    public void setPowerSource(int powerSource) {
        this.powerSource = powerSource;
    }

    public float getPricePerDay() {
        return this.pricePerDay;
    }

    public void setPricePerDay(float pricePerDay) {
        this.pricePerDay = pricePerDay;
    }


}
