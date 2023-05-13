class Person {
    String name;
    String address;
    String phone;
    int age;

    Person(String NewName, String address, String phone){
        this.name = NewName;
        this.address = address;
        this.phone = phone;
    }

    void setName(String name){
        this.name = name;
    }

    String getName(){
        return(name);
    }

    String getPhone(){
        return(phone);
    }

    public String toString(){
        return name + " " + address + " " + phone ;

    }

}
