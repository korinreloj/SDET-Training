### while: only one
# 1. syntax
# 2. condition
# 3. block of code

i = 20

while i >= 1:
    #print(i)
    i = i - 1

#---
i = 0

while i <= 48:
    i += 2
    print(i)

i = 0
while i <= 10:
    print(i)
    i = i + 1
else:
    print("this is the else")

### for loop: iterate in every element

fruits = ["mango", "apple", "orange"]

for x in fruits:
    print(x)

print("------")

cars = {"ferrari", "audi", "bmw", "ford"}

for x in cars:
    print(x)

print("------")
number = 0
divisor = 2

while number <= 50:
    if number % divisor != 0:
        print(number)
    number += 1
    divisor += 1

print("------")