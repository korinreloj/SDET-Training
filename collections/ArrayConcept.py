import array as arr
line = "------------------------"
x = min(10, 20, 30, 40, 50)
y = max(10, 20, 30, 40, 50)

print(x)
print(y)

#array with int type
a = arr.array('i', [1,2,3,4,5])
print(a)
print(type(a))

#access the element of array with the help of index
print(a[2])
print(line)

fruits = ["melon", "banana", "mango", "apple", "grapes", "orange"]
#for x in fruits:
#    print(x)

print(fruits[2])
print(line)

#remove value in array using index
fruits.pop(3)
print(fruits)
print(line)

#adds value in the end of array
fruits.append("Kiwi")
fruits.append("Lemon")
print(fruits)
print(line)

#another option to remove value in array
fruits.remove("Lemon")
print(fruits)
print(line)

#some common methods we use in array
#clear() - removes all the elements from the array
#copy - to copy the elements
#append - to add an element
#count - it returns the number of elements
#extend - add the elements to the end of the value
#index - returns the index of the specified element with the specified value
#insert - to add an element at specified position
#pop - to remove an element based on index
#remove - to remove an element based on the value
#reverse - to reverse the order of the list/array
#sort - to sort all the elements available