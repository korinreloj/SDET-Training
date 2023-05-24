class Constructor:

    first = 0
    second = 0
    third = 0

    #parameterized constructor
    def __init__(self, f, s):
        self.first = f
        self.second = s

    def display_result(self):
        print("The value of first number is:" + str(self.first))
        print("The value of second number is:" + str(self.second))
        print("The addition values of these two numbers are:" + str(self.third))

    def calculate(self):
        self.third = self.first + self.second

obj = Constructor(1000, 2000)
obj.calculate()
obj.display_result()
print("----")
obj1 = Constructor(5000, 6000)
obj1.calculate()
obj1.display_result()