# Default arguments are values that are provided while defining functions.
# The assignment operator = is used to assign a default value to the argument.
# Default arguments become optional during the function calls.
# If we provide a value to the default arguments during function calls, it overrides the default value.
# The function can have any number of default arguments.
# Default arguments should follow non-default arguments.
# def Main(x=10,y=20,z=30):
#     print('x value is :', x)
#     print('y value is :', y)
#     print('z value is :', z)
#
# Main()


# I ll passing one Argument
def Main(x=10,y=20,z=30):
    print('x value is :', x)
    print('y value is :', y)
    print('z value is :', z)

Main(12,14)
# x value is : 12
# y value is : 20
# z value is : 30