
# Python Identity Operators
# Identity operators are used to compare the objects, not if they are equal,
# but if they are actually the same object, with the same memory location:

x1 = [1,2,3,4,5,6,7]

x2 = [1,2,3,4,5,6]

# print(x1 == x2)
# True

# is 	Returns True if both variables are the same object

x3 = x1
# print(x3)
# [1, 2, 3, 4, 5, 6, 7]

print(x3 is x2)
False
print(x1 is x3)
True

x4 = x2

print(x4 is x3)
# False