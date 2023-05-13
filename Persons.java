import java.util.ArrayList;

public class Persons {

    ArrayList<Person> object_list;

    Persons(){
        object_list = new ArrayList<Person>();
    }


    public Persons search(String name) {
     
        Persons list = new Persons();
        for (Person cur : object_list){
            if (cur.getName().equals(name)){
             list.add(cur);
        }
    }
        return list;   
    }

    public void add(Person name){
        this.object_list.add(name);

    }

    int getSize(){
        return object_list.size();
    }

    public void delete(int i){
        this.object_list.remove(i);
    }

    public ArrayList<Person> getInternalList(){
        return object_list;
    }

}
