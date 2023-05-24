class test:

    def __init__(self):
        self.__salary = 1000

    def initialSalary(self):
        print("The initial salary for employee:", self.__salary)

    def newSalary(self):
        print("The new salary for employee:", self.__salary)

    def setNewSalary(self, salary):
        self.__salary = salary

employee1 = test()
employee1.initialSalary()
employee1.setNewSalary(2000)
employee1.newSalary()

employee1.setNewSalary(3000)
employee1.newSalary()

employee1.setNewSalary(5000)
employee1.newSalary()
