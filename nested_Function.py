"""
# nested Function
print ("before func 1 exicution")
def func1():
    print("this is func 1")
    def func2():
        print("this is func 2")
        return None
    func2()
    return None 
print("after the func1 exicution")

    #before func 1 exicution
    #after the func1 exicution  --- not call the function 
func1()
           #before func 1 exicutionc
           #after the func1 exicution
            #this is func 1
 """
 # examples 
"""
def calcy():
    def addition(a,b):
       return a + b
    def subtraction(a,b):
        return a - b
    def multiplication(a,b):
        return a * b 
    def division(a,b):
        return a / b
    def cube(a,b):
        return a ** b
    add = addition(2,3)
    sub = subtraction(5,3)
    mul = multiplication(4,7)
    div = division(10,2)
    cub2 = cube(4,6)
    print(add, sub, mul, div, cub2)
    return None
calcy()
# 5 2 28 5.0 4096

def func():
    def inner():
        print ("inside inner function")
    return inner
var = func()
var()
def outer(x):
    print("value of x",x)
    def inner(y):
        print ("value of y", y)
    inner(x * 2)
outer(5) 

""" 
  