

# for i in range(1,11):
#    print(list(i**2))
# print(x1)
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]



# TypeError: 'int' object is not iterable


# Map:
# syntax: map(functionName, iterable)

# The map() function in Python is a built-in function that applies a given function to each item of an iterable
# (e.g., a list, tuple, or string) and returns an iterator with the results.
#
# The syntax for the map() function is as follows:
#
# python
# Copy code
# map(function, iterable)
# The function parameter represents the function that you want to apply to each item of the iterable.
# It can be a built-in function or a user-defined function.
#
# The iterable parameter is the sequence of items you want to process. It could be a list, tuple, string, or any other iterable object.
#
# Here's a simple example to illustrate how the map() function works:


def Func(i):
    return i**2

x1 = [1,2,3,4,5,6,7,8,9,10]

m1 = map(Func,x1)
# print(m1)
# <map object at 0x0000025BC6B5B160>

# print(list(m1))
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# print(tuple(m1))
# (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)


