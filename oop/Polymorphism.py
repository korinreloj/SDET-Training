#method overloading
def product(a,b):
    p = a+b
    print(p)

def product(a, b, c):
    p = a+b+c
    print(p)

#product(2,4)
product(2,4,5)

from multipledispatch import dispatch
#method overriding
@dispatch(int, int)
def product(a,b):
    p = a+b
    print(p)

@dispatch(int, int,int)
def product(a, b, c):
    p = a+b+c
    print(p)

product(2,4)
product(2,4,5)

print("----------------")
stringTest = "SDET Batch"
print(len(stringTest))

list = ["a", "b", "d"]
print(len(list))


print("----------------")
class TestA:
    def first_Function(self):
        print("my function is available in class A")

    def second_Function(self):
        print("my function is available in class B")

#overriding the properties/methods of Class A
#multiple class of overriding
class TestB(TestA):
    #repetition of other method
    def first_Function(self):
        print("i am modifying this function in class B")

    def second_Function(self):
        print("i am changing second function in class B")

    def third_Function(self):
        print("my function is available in class B")


obj = TestB()
obj.first_Function()
obj.second_Function()
obj.third_Function()