x1 = {1,2,3,4,5,6,7,8}
print(type(x1))
# print('This is set:',x1)
# <class 'set'>
# This is set: {1, 2, 3, 4, 5, 6, 7, 8}

# Python frozenset() Method creates an immutable Set object from an iterable. It is a built-in Python function.
# As it is a set object therefore we cannot have duplicate values in the frozenset.


# Syntax : frozenset(iterable_object_name)
# Parameter : iterable_object_name
#
# This function accepts iterable object as input parameter.
# Return :  Returns an equivalent frozenset object.

x2 = frozenset(x1)
print(x2)
# frozenset({1, 2, 3, 4, 5, 6, 7, 8})
print(type(x2))
# <class 'frozenset'>


