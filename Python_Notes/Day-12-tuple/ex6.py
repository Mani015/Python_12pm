

s1 = {11,22,33,44,55,66,77,88,99,100}
print(s1)
# {33, 66, 99, 100, 11, 44, 77, 22, 55, 88}

# set add() method takes exatly one argumet to add the exisiting set
s1.add(101)
# print(s1)
# {33, 66, 99, 100, 101, 11, 44, 77, 22, 55, 88}



s1.add(102,103)
print(s1)
# TypeError: set.add() takes exactly one argument (2 given)
