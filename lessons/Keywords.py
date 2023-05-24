z = 50

if z>9:
    print("Value is correct")

i = 11
if i >15:
    print(i, "is greater")
else:
    print(i, "is less")

### nested if
i = 20

if i == 20:
    print("accepting value")
    if i < 10:
        print("yes print")
    else:
        print("first is satisfied but second is not")
else:
    print(i, "is less than 20")


### if else ladder (multiple conditions)
i= 16
if i == 15:
    print(i, "is equal to my value")
elif i > 15:
    print(i, "is greater than my value")
elif i < 15:
    print(i, "is less than my value")
else:
    print("unable to identify value")
