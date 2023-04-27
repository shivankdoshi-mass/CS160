from Person import Person

class Employee:
    def __init__(self, newName="none", address="none", phone="999-999-9999", department = "not assigned"):
        self.department = department
        self.name = newName

    def getDepartment(self):
        return (self.department)

    def setDepartment(self, department):
        self.department = department 

    def getName(self):
        return(self.name)