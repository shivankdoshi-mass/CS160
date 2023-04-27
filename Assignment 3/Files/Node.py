class Node:
    def __init__(self):
        self.previous = None
        self.next     = None
        self.data     = None

    def getData(self):
        return(self.data)

    def getNext(self):
        return(self.next)

    def getPrevious(self):
        return(self.previous)

    def setData(self, d):
        self.data = d

    def setNext(self, n):
        self.next = n

    def setPrevious(self, p):
        self.previous = p

    def __str__(self):
        return(str(self.getData()))
