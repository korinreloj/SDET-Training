#implement runtime polymorphism for the classs employee
# and change the designation of all the employees in  another class
# via separate methods for every employee

class Employee:
    def employee1_Designation(self):
        print("Designation: business")

    def employee2_Designation(self):
        print("Designation: business")

    def employee3_Designation(self):
        print("Designation: Marketing")

class EmployeeChange(Employee):
    def employee1_Designation(self):
        print("Updated Designation: IT")
    def employee2_Designation(self):
        print("Updated Designation: HR")
    def employee3_Designation(self):
        print("Updated Designation: Research")

employee = EmployeeChange()
employee.employee1_Designation()
employee.employee2_Designation()
employee.employee3_Designation()