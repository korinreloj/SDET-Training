line = "------------------"

z = "hi"
try:
    print(z)
except:
    print("Exception occurred and due to this, try code is not working")

print(line)

value1 = 1
value2 = 0
try:
    value = value1/value2
    print(value)
except Exception as e:
    print(e)

print(line)

try:
    print("Hello")
except:
    print("Something went wrong in try block")
else:
    print("Nothing went wrong anywhere")

print(line)

#else will only execute if try is true
try:
    value = value1/value2
    print(value)
except Exception as e:
    print(e)
else:
    print("Nothing went wrong anywhere")

print(line)

#finally block - after try and except condition if you wish to execute any block of code irrespective of the result of try - except, you keep this code in the finally block
try:
    print("Hello")
except:
    print("there is an error in the try")
else:
    print("I am running bcz try is good")
finally:
    print("I am running irrespective of the result of try and except")

print(line)

try:
    value = value1/value2
    print(value)
except:
    print("there is an error in the try")
else:
    print("I am running bcz try is good")
finally:
    print("I am running irrespective of the result of try and except")

print(line)

#raise - it is a keyword which allows us to create our own exceptions
x = -1
#if x<0:
    #raise Exception("Sorry, no negative values allowed in the program")

x = "hello"
if not type(x) is int:
    raise TypeError("Only integer values are allowed")