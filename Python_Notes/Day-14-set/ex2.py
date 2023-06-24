
z1 = {'apple','mango','orange','banana'}
print(type(z1),z1)

# <class 'set'> {'banana', 'apple', 'mango', 'orange'}

z2 = frozenset(z1)
print()
print(type(z2),z2)
# <class 'frozenset'> frozenset({'orange', 'mango', 'banana', 'apple'})


# union: combing the two frozent sets
# sy: fset.union(fset2)

print(z2.union({1,2,3,4,5,6,7}))

# frozenset({'mango', 1, 2, 3, 4, 'banana', 'orange', 5, 6, 7, 'apple'})
