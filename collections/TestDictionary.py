#create a dictionary named employee and print all the values
employee = {
    "empId": "67890",
    "name": "Lisa",
    "location": "Thailand",
    "designation": "Developer"
}
print(employee.values())
#then update the designation and emp id and print final data
employee.update({"designation": "QA"})
employee["empId"] = "37282"
print(employee)
#create another dictionary called cars and add 3 new cars in it
cars = {
    "car1": "toyota",
    "car2": "mitsubishi",
    "car3": "honda"
}
#now get all the keys and values from cars dict
cars["car4"] = "audi"
cars["car5"] = "porsche"
cars["car5"] = "nissan"
print(cars)

print("----------------")
#create a dict of 4 pair and check the existence of anyone from them
animal = {
    "name": "lizard",
    "species": "reptile",
    "color": "green",
    "action": "climb"
}

if "action" in animal:
    print("it is a key in animal dictionary")
else:
    print("not a key in animal dictionary")

#create a dict and remove any value from it with the help of function, with the help of key
mobile = {
    "brand": "samsung",
    "model": "S7",
    "ram": "8gb",
    "carrier": "Globe",
    "color": "silver"
}
mobile.pop("ram")
del mobile["carrier"]
print(mobile)
#define the difference between clear and del function in dict
#clear - delete all data in a collection
#del - delete a data/element or the actual collection

#create a dictionary of 5 pairs and copy it into another dict using built-in fucntion
book = {
    "title": "The Hunger Games",
    "author": "Suzanne Collins",
    "year": 2008,
    "genre": "Utopian",
    "publisher": "Scholastic"
}

new_book = dict(book)
print(new_book)

