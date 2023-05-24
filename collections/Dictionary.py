line = "------------------"
#syntax of how to declare dictionary
new_dict = {
    "name": "Timmy",
    "age": 35,
    "location": "Malibu",
    "country": "USA",
    "designation": "Lead",
    "employeeId": "12345"
}

print(type(new_dict))
print(new_dict)
print(line)

#update the dictionary
new_dict.update({"country": "Philippines"})
print(new_dict)
print(line)

#check length
print(len(new_dict))
print(line)

#access particular item from dict using the key
print(new_dict["name"])
print(line)

#another way to update value
new_dict["employeeId"] = "67890"
print(new_dict)
print(line)

#add items in the dictionary
new_dict["project"] = "Test"
new_dict["duration"] = "2 yrs"
print(new_dict)
print(line)

#access all the keys from dictionary
print(new_dict.keys())
print(line)

#access all the values from dict
print(new_dict.values())
print(line)

#get function to access value; only for key
print(new_dict.get("country"))
print(line)

#check the existence of key in the dictionary
employee = {
    "name": "Aditi",
    "designation": "Software Engineer",
    "country": "India",
    "project": "evert"
}

if "lead" in employee:
    print("it is a key in employee dictionary")
else:
    print("not a part of employee dictionary")

print(line)

car = {
    "brand": "Ford",
    "model": "Mustang",
    "logo": "standard",
    "year": 1984,
    "price": 52372
}

print(car)
print(line)

#remove value and key using function
car.pop("price")
print(car)
print(line)

#remove item from dict with specified key
car = {
    "brand": "Honda",
    "model": "City",
    "logo": "normal",
    "year": 1964,
    "price": 12345
}

del car["year"]
print(car)
print(line)

#delete entire dict
del car

#clear method
car = {
    "brand": "Honda",
    "model": "City",
    "logo": "normal",
    "year": 1964,
    "price": 12345
}

print(car.clear())
print(line)

#copy values from 1 dict to another
car = {
    "brand": "Honda",
    "model": "City",
    "logo": "normal",
    "year": 1964,
    "price": 12345
}

new_car = car.copy()
print(new_car)
print(line)

#another way to copy using built in function
car1 = {
    "brand": "Honda",
    "model": "City",
    "logo": "normal",
    "year": 1964,
    "price": 12345
}

car2 = dict(car1)
print(car2)