
# Keyword Arguments in Python
# Functions can also be called using keyword arguments of the form kwarg=value.
#
# During a function call, values passed through arguments don’t need to be in the order of parameters in the function definition.
# This can be achieved by keyword arguments.
# But all the keyword arguments should match the parameters in the function definition.

# syntax:
# def f1(key1,key2,key3):
#     print(body of fun)
# f1(key1 = value1,key2 = value2,key3=value3)


def Fun(x,y,z):
    print('x value is :',x)
    print('y value is :',y)
    print('z value is :',z)

# Fun(x = 10,y = 20,z = 30)
#x value is : 10
# y value is : 20
# z value is : 30



