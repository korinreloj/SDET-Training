line = "----------------"
#Define a set of 7 values and identify one specific value from it
groceries = {"milk", "cereal", "soap", "shampoo", "laundry detergent", "orange juice", "chips"}
print("shampoo" in groceries)

#create a set of having multiple data types
sample_set = {1, 4, -77, False, "Hello", 2.901}
print(sample_set)

#create a set of 5 values and add 2 more values later in it
office_supplies = {"pencil", "memo pad", "sticky notes", "tape", "notebook"}
office_supplies.add("ballpoint pen")
office_supplies.add("eraser")
print(office_supplies)
print(line)


#Create a set of 5 elements and add a list of 3 elements in it
supplies_set = {"pencil", "memo pad", "sticky notes", "tape", "notebook"}
supplies_list = ["stapler", "eraser", "ballpoint pen"]
supplies_set.update(supplies_list)
print(supplies_set)


#remove the value from the set of 10 elements using both the methods
animals_set = {"jose", "frog", "tiger", "cat", "dog", "mouse", "lizard", "maria", "horse", "pig"}
animals_set.remove("jose")
animals_set.discard("maria")
print(animals_set)


#define a set and delete the set from the memory
new_set = {1, 2, 3, 4, 5}
del new_set
print(new_set)


#create 2 set and print only unique elements from there
clothes_set1 = {"pants", "shirt", "sneakers"}
clothes_set2 = {"skirt", "dress", "sneakers", "shirt"}
clothes_set1.union(clothes_set2)
print(clothes_set1)


#create 2 sets and print only duplicate values from there
drinks_set1 = {"cappucino", "berry smoothie", "water"}
drinks_set2 = {"orange juice", "berry smoothie", "water"}
drinks_set1.intersection_update(drinks_set2)
print(drinks_set1)

#create 2 sets and print all the elements together
flavors_set1 = {"sweet", "sour", "spicy"}
flavors_set2 = {"salty", "spicy", "bitter"}
flavors_set1.symmetric_difference_update(flavors_set2)
print(flavors_set1)
