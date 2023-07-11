from functools import reduce

r1=reduce(lambda a,b:a+b,filter(lambda k:k%2==0,map(lambda i:i**2,range(1,101))))
# print(r1)



# Python Variable Scope
# In Python, we can declare variables in three different scopes: local scope, global, and nonlocal scope.
#
# A variable scope specifies the region where we can access a variable. For example,
#
# def add_numbers():
#     sum = 5 + 4
# Here, the sum variable is created inside the function,
# so it can only be accessed within it (local scope). This type of variable is called a local variable.
#
# Based on the scope, we can classify Python variables into three types:
#
# Local Variables
# Global Variables
# Nonlocal Variables(Enclosing Variable)
# Built-in varaible


a = 1
b  =2
# a = 3
# print(a)
# 3

def f1():
    a = 20
    print(a)
f1()
print('outside function:',a)
# 20
# outside function: 1
