public class Employee extends Person{
    String name;
    String address;
    String phone;
    String department; 

    public Employee(String NewName, String address, String phone, String department){
        super(NewName, address, phone);
  
        this.department = department;

    }

    public String toString(){
        return name + " " + address + " " + phone + " " + department; 
    }

    String getDepartment(){
        return(department);
    }

    void setDepartment(String department){
        this.department = department;
    }

}
