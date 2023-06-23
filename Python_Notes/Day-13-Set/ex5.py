# isdisjoint()	Returns whether two sets have a intersection or not
z1 = {1,2,3,4,5,6,7,8,9}
z2 = {11,22,33,44,55,1,2,3,4}
# True: both sets are complete difference it will return True
# False: both sets same like at least one elemnet it will return Fasle
# syntax: set1.isdisjoint(set2)

# print(z1.isdisjoint(z2))
# False


# True: both sets are complete difference it will return True
print({1,2,3,4,5,6}.isdisjoint({11,22,33,44,55}))
# True
