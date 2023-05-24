class Food:
    def honey_food(self):
        print("Honey is a food used to sweeten")

class Medicine:
    def honey_medicine(self):
        print("Honey is a traditional medicine")

class Honey(Food, Medicine):
    def honey_food_medicine(self):
        print("Honey is both a medicine and food")

honey = Honey()
honey.honey_food()
honey.honey_medicine()
honey.honey_food_medicine()