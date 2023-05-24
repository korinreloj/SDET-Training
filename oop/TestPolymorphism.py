from multipledispatch import dispatch
#1. addition of 3 int
@dispatch(int,int,int)
def operation(a, b ,c):
    sum = a + b + c
    print(sum)

#2. multiply 3 float values
@dispatch(float,float,float)
def operation(a, b ,c):
    product = a * b * c
    print(product)

#3. addition of 4 int values
@dispatch(int,int,int,int)
def operation(a, b,c,d):
    sum = a + b + c + d
    print(sum)

#4. multiply 4 double values
@dispatch(float,float,float,float)
def operation(a, b, c, d):
    product = a * b * c * d
    print(product)

operation(1, 2, 3)
operation(2.0, 3.0, 7.0)
operation(1, 2, 3, 4)
operation(1.0, 2.0, 3.0, 2.0)