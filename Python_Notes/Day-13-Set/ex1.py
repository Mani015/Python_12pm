
# difference()	Returns a set containing the difference between two or more sets

s1  = {1,2,3,4,5,6,7,11,22,33,44}
s2 = {1,2,3,4,5,6,7,55,66}

# syntax:set1.differece(set2)
# print(s1.difference(s2))
# {33, 11, 44, 22}
# s1-s2


# print(s2.difference(s1))
# {66, 55}

x1 = {'shiva','ramu','dinesh','vinod','bhaskar'}
x2 = {'vishal','dhamu','jakir','vinod'}

print(x1.difference(x2))
# {'ramu', 'bhaskar', 'dinesh', 'shiva'}
print(x2.difference(x1))
# {'vishal', 'jakir', 'dhamu'}
