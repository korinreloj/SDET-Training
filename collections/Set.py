line = "----------------"
#syntax
set_example = {"nette", "ezra", "kim", "ivy"}
#type of collection
print(type(set_example))
print(set_example)
print(line)

#no duplicates
example = {"timmy", "honey", "kim", "ezra", "timmy", "ezra"}
print(example)
print(line)

#check length for duplicates
new_set = {"", "", "", "", "kim", "honey", "hizelle"}
print(new_set)
print(len(new_set))
print(line)

#use of 'in' keyword in set
employee = {"kim", "ivy", "jerica", "nette", "timmy"}
print("ivy" in employee)
print(line)

#add value
test = {"ezra", "honey", "hydeline", "jerica"}
print(test)
test.add("timmy")
print(test)
print(line)

#set supports/allows multiple data types while implementing it
set1 ={"timmy", "honey", "jerica", "kim"}
print(type(set1))
set2 = {1, 2, 3, 7, 9}
print(type(set2))
#True and False are flags
set3 = {True, False, True, False}
print(type(set3))
print(line)

#+ operator will not work
#set3 = set1 + set2

#flags will not print true
mix_set = {"timmy", "nette", 1, 2, 3, False, 6, True, "ezra"}
print(mix_set)

#using double round brackets (type casting)
this_set = set(("abc", "xyz", "abc"))
print(this_set)
print(line)

#using if condition to check value if it is in the set
newset = {"kim", "jerica", "joammme", "ivy", "symonds"}
x = "symonds"

if x in newset:
    print(x)

print(line)

#combine two sets
set1 = {"apple", "banana", "cherry", "grapes"}
set2 = {"lemon", "melon", "berries", "pineapple"}

set1.update(set2)
print(set1)

#list + set is possible
mynewset = {"timmy", "ezra", "jerica", "hizelle", "nette"}
mynewlist = ["honey", "shane", "kim", "ivy", "jerica"]

mynewset.update(mynewlist)
print(mynewset)
print(line)

#remove the item from the set
employee = {"timmy", "kim", "ivy", "sohel", "symonds"}
print(employee)
employee.remove("sohel")
employee.discard("symonds")
print(employee)
print(line)

#clear - make the set empty, delete all values
employee = {"timmy", "kim", "ivy", "sohel", "symonds"}
employee.clear()
print(employee)
print(line)

#delete set - will delete set from the memory
employee = {"timmy", "kim", "ivy", "sohel", "symonds"}
del employee
#print(employee)


#join 2 sets together
set1 = {"jim", "kim", "timmy", "jerry", "honey"}
set2 = {"jerica", "honey", "nette", "kim"}

#using union - it will keep unique values
set3 = set1.union(set2)
print(set3)
print(line)

#use interaction - values that can be found in both sets
set1 = {"jim", "kim", "timmy", "jerry", "honey"}
set2 = {"jerica", "honey", "nette", "kim"}
set1.intersection_update(set2)
print(set1)
print(line)

#symmetric diffrence update - only the ones not common in both sets
set1 = {"jim", "kim", "timmy", "jerry", "honey"}
set2 = {"jerica", "honey", "nette", "kim"}
set1.symmetric_difference_update(set2)
print(set1)