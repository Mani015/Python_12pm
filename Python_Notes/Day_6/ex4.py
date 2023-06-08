# is not: Returns False if both variables  same object

x = ['a','b','c','d']

y = ['x','y','z']

z = x
# print(z)
# ['a', 'b', 'c', 'd']

print(z is not y)
# True
print(y is not y)
# False

print(x is not a)
# NameError: name 'a' is not defined
