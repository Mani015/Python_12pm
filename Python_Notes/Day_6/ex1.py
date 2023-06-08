
# Python Membership Operators
# Membership operators are used to test if a sequence is presented in an object:
# There are two keywords
import keyword
# print(keyword.kwlist)
# ['False', 'None', 'True', '__peg_parser__', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']


python = ['Bhaskar','sai vinod','Vishal','Dhamu','Dinesh']

# member is present in python(family) it will returns True
# in: Returns True if a sequence with the specified value is present in the object
print('Dhamu' in python)
# True

print('Vishal' in python)
# True

print('Bharath' in python)
# False
