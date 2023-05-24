class Bird:
    def __init__(self):
        print("Bird is available in parent class")

    def which_Bird_Is_This(self):
        print("Identifying bird in parent class")

    def swim_Bird(self):
        print("Bird is swimming in parent class")

class Penguin(Bird):
    def __init__(self):
        #call super() for parent class
        super().__init__()
        print("Penguin child id ready in child class")

    def which_Class_Is_This(self):
        print("It is in child class")

peng = Penguin()
peng.which_Bird_Is_This()
peng.which_Class_Is_This()
peng.swim_Bird()