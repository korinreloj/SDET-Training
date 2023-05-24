#modulo returns whole number
x = 5
y = 10
print(y//x)

y = 5
y*=5
print(y)

a=10
a/=5
print(a)

#comparison
print(x==5)
print(x!=5)
print(x)
print(a)
print(x>a)
print(x>=a)
print("yes x value is greater:", x)

###logical
text1 = "hi"
text2 = "hi"

a = 8
b = 10
if text1 == text2 or a == b:
    print("atleast one condition is equal")

if text1 == text2 and a == b:
    print("both conditions are equal")

### identity
list1 = ["fruit", "shoes", "clothing"]
list2 = ["fruit", "shoes", "clothing"]

# list2 = list1
print(list1 is list2)

### membership
list1 = ["fruit", "shoes", "clothing"]
list2 = ["fruit"]
string1 = "fruit"

print ("membership:", list2 in list1)
print ("membership:", string1 in list1)

