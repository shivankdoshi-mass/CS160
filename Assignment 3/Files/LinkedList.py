from Node import Node
from Person import Person

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def search (self, name):
        newLinkedList = LinkedList()
        result_head = None
        current = self.head 
        while current is not None:
            if current.getData().getName() == name:
                newLinkedList.add(current.getData())                
            current = current.getNext() 
        return newLinkedList  

    def add(self, e):
        n = Node()
        n.setData(e)
        if self.size == 0:
            self.head = n
            self.tail = n
        else:
            currentlyTheLastElement      = self.tail
            n.setPrevious(currentlyTheLastElement)
            currentlyTheLastElement.setNext(n)
            self.tail                    = n
        self.size = self.size + 1
                

    def insert(self, index, data):
        newNode = Node()
        newNode.setData(data)
        if index > (self.length()):
            return
        if (index == 0):
            if self.head == None:
                self.head = newNode
                self.tail = newNode
            else:
                newNode.setNext(self.head)
                self.head.setPrevious(newNode)
                self.head = newNode

        elif (self.length() == index):
            self.tail.setNext(newNode)
            newNode.setPrevious(self.tail)
            newTail = self.tail
            self.tail = newNode
        else:
            i = 0
            current = self.head 

            while (i < index):
                i += 1 
                current = current.getNext()               


            previous = current.getPrevious() 
            previous.setNext(newNode)
            current.setPrevious(newNode)
            newNode.setNext(current)
            newNode.setPrevious(previous)

        self.size += 1

    def length(self):
        return(self.size)


    def __getitem__(self, i):
        currentElement = self.head
        howManyIHaveSkippedOver = 0
        while (howManyIHaveSkippedOver < i):
            currentElement          = currentElement.next
            howManyIHaveSkippedOver = howManyIHaveSkippedOver + 1
        return(currentElement.getData())


    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next


    def __str__(self):
        stringToReturn = ""
        for e in self:
            stringToReturn = stringToReturn + str(e) + "\n"
        return(stringToReturn)
    

    def delete(self, i:int):
        if i > (self.length()-1):
            return
        elif i == 0:
            temp = self.head.getNext()
            self.head = temp 
            if temp == None:
                return
            else:                 
                temp.setPrevious(None)
        elif i == self.length()-1:
            temp = self.tail.getPrevious()
            self.tail = temp
            if temp == None:
                return 
            else: 

                temp.setNext(None)
        else:
            current = self.head
            count = 0
            while count < i and current and current.getNext():
                current = current.getNext()
                count += 1
            nxt = current.getNext()
            prev = current.getPrevious()
            prev.setNext(nxt)
            nxt.setPrevious(prev)


if __name__== "__main__":
    samplePerson1 = Person("Jaime", "Crashboat Beach", "111-222-3333")
    samplePerson2 = Person("maria", "cape cod", "111-222-3333")
    samplePerson3 = Person("Jaime", "Malibu Beach", "something else")
    samplePerson4 = Person("an element to add", "somewhere", "999-999-9999")
    
    myLinkedList = LinkedList()
    print("the size of this list is", myLinkedList.length())
    myLinkedList.add(samplePerson1)
    print("after adding samplePerson1, the size of this list is", myLinkedList.length())
    myLinkedList.add(samplePerson2)
    myLinkedList.add(samplePerson3)
    myLinkedList.add(samplePerson4)
    print(myLinkedList[2])
    print(myLinkedList.search("maria"))

    listOfIntegers = LinkedList()
    listOfIntegers.add(1)
    listOfIntegers.add(7)
    listOfIntegers.add(-2)
    listOfIntegers.add(42)
    listOfIntegers.insert(0, 0)
    print(listOfIntegers)
    listOfIntegers.delete(3)
   
