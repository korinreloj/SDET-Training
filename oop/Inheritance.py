# single inheritance

#base class, parent class, super class
class Parent:
    def first_Function(self):
        print("this function is available in parent class")

class Child(Parent):
    def second_Function(self):
        print("this function is available in child class")

object = Child()
object.first_Function()
object.second_Function()

print("-----------------------")
#multiple inheritance

class Mother:
    mothername = ""
    def mother(self):
        print(self.mothername)

class Father:
    fathername = ""
    def father(self):
        print(self.fathername)

class Son(Mother, Father):
    def parents(self):
        print("Father : ", self.fathername)
        print("Mother : ", self.mothername)

son = Son()
son.fathername = "Rogelio"
son.mothername = "Corazon"
son.parents()