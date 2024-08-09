class Employee:
    def __init__(self,name,salary=20000):
        self.name = name
        self.salary = salary
    def printInfo(self):
        print(self.name,self.salary)
emp1 = Employee("Sean",50000)
emp1.printInfo()
emp2 = Employee("Vivin",36000)
emp2.printInfo()
