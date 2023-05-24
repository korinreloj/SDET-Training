#Write a program to check whether the number is Armstrong or not?
number = 370
number_chars = list(str(number))
sum = 0

for i in number_chars:
    new_num = int(i)
    sum = (new_num ** 3) + sum

if number == sum:
   print(number,"is an Armstrong number")
else:
   print(number,"is not an Armstrong number")

#Write a Python program to reverse the order of the items in the array?
array = ["a", "b", "c", "d", "e"]
array.reverse()
print(array)

#WAP to Cloning a list?
veggies = ['garlic','onion','cabbage', 'radish','potato','squash','broccoli']
new_veggies = veggies.copy()
print(new_veggies)

#Write a program to print even numbers from 0 to 100?
i = -2

while i <= 98:
    i += 2
    #print(i)

#Write a program to print right angle triangle?
rows = 5
for i in range(rows):
    for j in range(i + 1):
        print("+", end=" ")
    print()

#Write a program to find the area of triangle where values are a=5, b=6, c=7
import math
a = 5.0
b = 6.0
c = 7.0

semi_perimeter = (a + b + c) / 2.0
area = math.sqrt(semi_perimeter*(semi_perimeter - a)*(semi_perimeter - b)*(semi_perimeter - c))
print(area)

#Write a program to check a leap year
year = 2020

if year % 4 == 0:
     if year % 100 != 0 or year % 400 == 0:
        print(year, "is a leap year")
else:
    print(year, "is not a leap year")

#Write a program to print Fibonacci series till 50?
limit = 50
a = 0
b = 1
while a <= limit:
    print(a)
    container = a + b
    a = b
    b = container
#WAP to display both the keys and values sorted in alphabetical order by the key.
mobile = {
    "brand": "samsung",
    "model": "S7",
    "ram": "8gb",
    "carrier": "Globe",
    "color": "silver"
}

sort_mobile = sorted(mobile.items())
print(sort_mobile)
#Write a Python Program to Remove Punctuations From a String?
string = "He!!o World!!"
punctuation = "!"
new_string = string.replace(punctuation, "")
print(new_string)
#WAP to reverse the list in a python?
list = [-5, 2, 3, 9, 100, 0]
list.reverse()
print(list)
#WAP to remove the whitespaces from the string?
string = "     hello world   "
print(string.strip())
#Write a Python program to get the number of occurrences of a specified element in an array?
array = ["Alex", "John", "Maria", "Brenda", "John", "John"]
print("Number of times element is present: ", array.count("John"))
#WAP to create a dictionary and display its keys alphabetically?
book = {
    "title": "The Hunger Games",
    "author": "Suzanne Collins",
    "year": 2008,
    "genre": "Utopian",
    "publisher": "Scholastic"
}
sort_book = sorted(book)
print(sort_book)
#WAP to return a new set of identical items from a given two set?
set1 = {"red", "orange", "yellow", "green", "indigo"}
set2 = {"indigo", "violet", "yellow", "red"}
set1.intersection_update(set2)
print(set1)

#WAP to reverse the following list using for loop - list = [10, 20, 30, 40, 50]
list = [10, 20, 30, 40, 50]
new_list = []

for i in list:
    new_list.insert(0, i)

print(new_list)