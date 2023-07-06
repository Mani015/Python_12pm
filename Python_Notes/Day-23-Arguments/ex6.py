
# What Are Variable-Length Arguments in Python?
# Variable-length arguments are also known as arbitrary arguments.
# If we don’t know the number of arguments needed for the function in advance, we can use arbitrary arguments
#
# THERE ARE TWO TYPES OF ARBITRARY ARGUMENTS:
# Arbitrary positional arguments.
# Arbitrary keyword arguments



# ARBITRARY POSITIONAL ARGUMENTS IN PYTHON
# For arbitrary positional argument, an asterisk (*) is placed before a parameter in function definition
# which can hold non-keyword variable-length arguments. These arguments will be wrapped up in a tuple.
# Before the variable number of arguments, zero or more normal arguments may occur.

def f1(x,y):
    print(x,y)

# f1(1,2)
# 1 2
# f1(1,2,3)
# TypeError: f1() takes 2 positional arguments but 3 were given