line = "------------------------"

my_list = ["corinne", "ezra", "joamm", "nette", "honey", "kim"]
print(my_list)
print(line)

#check the type
print(type(my_list))
print(line)

#access the value from the list based on index
print(my_list[1])
print(len(my_list))
print(line)

#assign value to my list
my_list[0] = "hizelle"
print(my_list)
print(line)

#insert new element
my_list.append("corinne")
print(my_list)
print(line)

#insert new element at a particular position in the list
my_list.insert(4, "ivy")
print(my_list)
print(line)

#range
list1 = ["toyota", "maruti", "suzuki", "mitsubishi", "bmw", "audi"]
print(list1[1:4])
print(line)


#change and add the values
#overwrite multiple values
bikes = ["honda", "bmw", "vespa", "kymco", "yamaha"]
print(bikes)
bikes[1:3] = ["suzuki", "hero"]
print(bikes)
print(line)

#insert item in the list at a particular position without overwritinbg anything
fruits = ["banana", "melon", "apple"]
fruits.insert(2, "lemon")
print(fruits)
print(line)

#append element from one list to another list
list1 = [ "apple","banana", "melons", "grapes"]
list2 = [ "lemon","orange", "pineapple", "cherry"]

list1.extend(list2)
print(list1)
print(line)

#remove element using the value from the list
mylist = ["apple", "banana", "orange"]
mylist.remove("orange")
print(mylist)
print(line)

#remove element using index
fruit = ["apple", "banana", "melon", "lemon"]
fruit.pop(2)
print(fruit)
print(line)

#del method also removes the specified index
listnew = ["timmy", "ezra", "ivy", "honey"]
del listnew[2]
print(listnew)
print(line)

#clear method - removes all elements
list = ["kim", "joamm", "nette"]
list.clear()
print(list)
print(line)

#list comprehension
fruits = ["lemon", "melon", "apple", "banana"]
new_fruit = []

for x in fruits:
    if "n" in x:
        new_fruit.append(x)

print(new_fruit)
print(line)

#sort the list alphabetically
fruits = ["lemon", "melon", "banana", "kiwi"]
fruits.sort()
print(fruits)

fluency = [67, 12, 44, 99, 79]
fluency.sort()
print(fluency)

fluency.sort(reverse=True)
print(fluency)

fruits = ["apple", "banana", "orange", "grapes", "melon", "pineapple"]
fruits.reverse()
print(fruits)
print(line)

#copy
emp = ["ezra", "kim", "timmy", "nette", "ivy"]
newemp = emp.copy()
print(newemp)

list1 = ["ezra", "jerica", "timmy", "ivy"]
list2 = [1, 2, 4, -4]

list3 = list1 + list2
print(list3)
print(line)

list1 = ["ezra", "hizelle", "jerica"]
list2 = ["timmy", "ms", "kim"]

for x in list2:
    list1.append(x)
print(list1)
