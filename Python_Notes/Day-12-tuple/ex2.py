# Tuple
# Tuples are used to store multiple items in a single variable.
#
# Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.
#
# A tuple is a collection which is ordered and unchangeable.
#
# Tuples are written with round brackets.
t1 = ()
# print(type(t1))
# <class 'tuple'>



t2 = (1,2,3,4,5,6,7,8)
print(t2)
# (1, 2, 3, 4, 5, 6, 7, 8)


t3 = ('saikiran','dhamu','vishal','myself')
# print(t3)
# t3.count('saikiran')
print(t3.count('saikiran'))
# 1
print(t3.count('virat'))
# 0

# Indexing

print(t3.index('dhamu'))
# 1

