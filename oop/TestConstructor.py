class test:

    def __init__(self, firstName, lastName, role):
        self.firstName = firstName
        self.lastName = lastName
        self.role = role

    def display_details(self):
        print("Employee information: " + self.firstName + " " + self.lastName + ", " + self.role)

employee1 = test("Liza", "Mariano", "PM")
employee1.display_details()
employee2 = test("June", "Soberano", "Scrum Master")
employee2.display_details()
employee3 = test("Mario", "Maurer", "Business Analyst")
employee3.display_details()
employee4 = test("Kim", "Hennah", "Developer")
employee4.display_details()
employee5 = test("Maria", "Smith", "Tester")
employee5.display_details()