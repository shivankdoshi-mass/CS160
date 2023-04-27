import Person
import Persons
import unittest

class Test(unittest.test):

    def testadd(self):
    
        Person1 = Person.Person("Maria", "Amherst", "111-111-1111", "CICS", 15)
        self.assertEquals(Person1, [Person])        
    
    def testdelete(self):    

        Person1 = Person.Person("Maria", "Amherst", "111-111-1111", "CICS", 15)
        Person2 = Person.Person("Eric", "Amherst", "111-111-1111", "CICS", 15)
        Person3 = Person.Person("John", "Amherst", "111-111-1111", "CICS", 15)
        list = [Person1, Person2, Person3]
    
        list.remove("Maria")
        list = [Person2]
        self.assertEquals(list, [Person2])

    def testsearch(self):
        self.assertEqual(len(Persons.search("Maria")))

    def testmodify(self):
    
       Person1 = Person.Person("Maria", "Amherst", "111-111-1111", "CICS", 15)
       Person1.setName("Lisa") 
       Person1.setLocation("Boston")      

       self.assertEquals("Lisa", Person1.getName())
    
    def testdisplay(self):
    
        Person1 = Person.Person("Lisa", "Amherst", "111-111-1111", "CICS", 15)
        self.assertEquals("Lisa", Person1.getName())
        self.assertEquals("CICS", Person.getCollege)



if __name__ == "__main__":
    p1 = Person.Person("Jaimee")
    Person1 = add(p1)
