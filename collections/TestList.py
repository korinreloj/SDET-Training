#create a list of 10 elements  and remove 5th element from it and del 4th element using pop method
flowers1 = ["rose", "magnolia", "daisy", "tulip", "lily", "hydrangea", "carnation", "sunflower", "orchid", "daffodil"]
flowers1.remove("lily")
flowers1.pop(3)

#creat another list and append new list in it
flowers2 = ["camellia", "chrysanthemum", "violet"]
flowers1.extend(flowers2)
print(flowers1)

#create another list and print the values from 2:7 range
veggies = ['garlic','onion','cabbage','bell pepper','ginger','corn', 'carrot', 'radish','potato','squash','broccoli']
print(veggies[2:7])

#create list of 5 elements and override 2 values with 3 new values in the list
employees = ["dora", "linda", "maria", "cora", "teresa"]
employees[2:4] = ["john", "alex"]
print(employees)

#create item in the existing list on a specified index position
snacks = ["chocolate", "chips", "candy"]
snacks.insert(2, "biscuit")
print(snacks)
print("--------------")

#create a list of 5 elements and identify the elements having common letter "a"
flowers = ["camellia", "chrysanthemum", "violet", "rose", "daisy"]
flowers_with_a = []
for x in flowers:
    if "a" in x:
        flowers_with_a.append(x)

print(flowers_with_a)

#create a list of 5 int values and print them in decreasing order
numbers = [1, 5, 0, -5, 23]
numbers.sort(reverse=True)
print(numbers)

#create a list of 10 elements and copy them into another list
veggies = ['garlic','onion','cabbage','bell pepper','ginger','corn', 'carrot', 'radish','potato','squash','broccoli']
new_veggies = veggies.copy()
print(new_veggies)

#add 2 list together
snacks1 = ["chocolate", "chips", "candy"]
snacks2 = ["popcorn", "fries", "milk tea"]

all_snacks = snacks1 + snacks2
print(all_snacks)