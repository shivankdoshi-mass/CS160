public class Student extends Person{
    String name;
    String address;
    String phone;
    int year; 

   

    public Student(String NewName, String address, String phone, int year){
        super(NewName, address, phone);

        this.year = year;

    }

    public String toString(){
        return name + " " + address + " " + phone + " " + year; 
    }

    int getGraduationYear(){
        return(year);
    }

    void setGraduationYear(int year){
        this.year = year;
    }


}
