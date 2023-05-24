#Create a block of code which should give syntax error
#uncomment to see syntax error
#x = 1/
#try:
    #print(x)

#create a code with except condition and else condition and execute try and else
value1 = 1
value2 = 9
try:
    value3 = value1 + value2
    print(value3)
except:
    print("This is the except block")
else:
    print("This is the else block")

#Write a program to execute finally block of code
value1 = 1
value2 = 9
try:
    value3 = value1 * value2
    print(value3)
except:
    print("This is the except block")
finally:
    print("This is the finally block")

#Write a program to create customized error for false arithmetic operations
value1 = 10
value2 = 0

try:
    value3 = value1 / value2
except:
    raise ArithmeticError("Encountered Arithmetic Error")