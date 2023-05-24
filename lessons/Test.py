a = 5
A = 7

print(a)
print(A)

a =0.5
print(type(a))

my_var_2 = ["he", 1, 0.5]
print(type(my_var_2))
print(my_var_2)

if "apple" in "apple of my eye":
    print("hi")
    print("apple")
print("no apples for u")

if "jams" not in "strawberry":
    print("u got no jams")

if "languge" not in "Python is a programming language":
    print("languge not present")

a = "123"
b = "abcde"
print(a + b)

text = "ibm is a leading sw product org"
print(text[2:90])

quantity = 5
itemNumber = "728AB"
price = 34.09

message = "Order quantity: {} item: {} price: {}"
print(message.format(quantity, itemNumber, price))

firstName = "Corinne"
middleName = "Soberano"
lastName = "Reloj"
designation = "QA"
message = "The details of the employee is: {} {} {}, {}"
print(message.format(firstName, middleName, lastName, designation))

message = "My sdet batch is learning python"
print(message[26:32])
print(len(message))

message = "      this is testing world        "
print(message.strip())

message = "This is software testing"
print(message.find("n"))