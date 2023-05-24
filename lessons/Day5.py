### practice 1
list1 = ["gadgets", "food", "clothing"]
list2 = ["decors", "household items"]

print(list1 is not list2)

### practice 2
list1 = ["mango", "banana", "kiwi"]

if "grapes" not in list1:
    print("true")
if "kiwi" in list1:
    print("true")

### practice 3
###A company decided to give bonus of 5% to the
# employees if their total years of service is more than 5 years.
# Ask the employee for the salary and year of services and
# print the net bonus of them
salary = 200
years = 10
bonus = 0.05

if years >= 5:
    net_bonus = salary + (salary * bonus)
    print("total salary:", net_bonus)

### take values of length and breadth
# of a rectangle and check if it is square or not

length = 5
width = 5

if length == width:
    print("this is square")
else:
    print("this is rectangle")

### take 3 values and print the greatest one among them
a = 1
b = 2
c = 3


if a > b and a > c:
    print(a, "is the greatest")
elif b > a and b > c:
    print(b, "is the greatest")
else:
    print(c, "is the greatest")