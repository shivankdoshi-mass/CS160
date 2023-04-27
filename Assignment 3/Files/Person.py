from operator import indexOf
import random
from xmlrpc.client import Boolean

class Person:
    def __init__(self, newName="none", address="none", phone="999-999-9999"):
        self.name = newName
        self.address = address
        self.phone = phone

    def setName(self, name):
        self.name = name

    def getName(self):
        return(self.name)

    def getPhone(self):
        return(self.phone)

    def __str__(self):
        stringtoReturn = "Name         : " + self.name \
                       + "\naddress      : " + self.address \
                       + "\nphone        : " + self.phone 
        return(stringtoReturn)

    def getData(self):
        self.name         = input("Enter name                         : ")
        self.address      = input("Enter address                      : ")
        self.phone        = input("Entr phone (in xxx-xxx-xxxx format): " )

    def __eq__(self, o):
        if (isinstance(o, Person)):
            return(self.getPhone() == o.getPhone())
        else:
            if (isinstance(o,str)):
                return(self.getPhone()== o)
            else:
                return(False)

    # def __eq__(self, s):
    #     return(self.getPhone() == s)

    def __ne__(self, o: object) -> bool:
        return(not(self==o))

    def __lt__(self, other)->Boolean:
        if (isinstance(other, Person)):
            return(self.getPhone() < other.getPhone())
        else:
            if (isinstance(other, str)):
                return(self.getPhone() == other)
            else:
                print("you're calling __lt__ with bad input, so it'll return False. YIKES!!!!")
                return(False)


if __name__== "__main__":
    samplePerson1 = Person("Jaime", "Malibu Beach", "111-222-3333")
    samplePerson2 = Person("maria", "cape cod", "111-222-3333")
    samplePerson3 = Person("Jaime", "Malibu Beach", "something else")
    print(samplePerson1 == samplePerson2)
    print(samplePerson1 == samplePerson3)
    print("are 1&2 different?", samplePerson1!=samplePerson2)

    # let's now do some strange stuff with lists.
    # let's put three objects into a list.
    sampleList = [samplePerson1, samplePerson2, samplePerson3]
    print (sampleList)
    # indexOfItemBeingProcessed = 0
    # #for o in sampleList:
    # for index in range(len(sampleList)):
    #     print("processing", indexOfItemBeingProcessed)
    #     sampleList.append("adding stuff inside the for loop")
    #     indexOfItemBeingProcessed = indexOfItemBeingProcessed+1
    # print(sampleList)

    # indexOfItemBeingProcessed = 0
    # for index in range(len(sampleList)):
    #     print("will delete item", indexOfItemBeingProcessed)
    #     sampleList.pop(indexOfItemBeingProcessed)
    #     print("now the list is", sampleList)
    #     indexOfItemBeingProcessed = indexOfItemBeingProcessed+1
    indexOfItemBeingProcessed = 0
    for o in sampleList:
        print("will delete item", indexOfItemBeingProcessed)
        sampleList.pop(indexOfItemBeingProcessed)
        print("now the list is", sampleList)
        indexOfItemBeingProcessed = indexOfItemBeingProcessed+1

    indexOfItemBeingProcessed = 0
    # while (indexOfItemBeingProcessed<len(sampleList)):
    #     print("processing element", indexOfItemBeingProcessed)
    #     sampleList.append("one more")
    #     indexOfItemBeingProcessed = indexOfItemBeingProcessed + 1
        


