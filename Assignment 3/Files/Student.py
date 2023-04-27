from Person import Person

class Student:
    def __init__(self, newName="none", address="none", phone="999-999-9999", year = 1999):
        self.name = newName
        self.address = address
        self.phone = phone
        self.year = year 

    def getGraduationYear(self) -> int:
        return (self.year)
    
    def setGraduationYear(self, year):
        self.year = year

    def getName(self):
        return(self.name)