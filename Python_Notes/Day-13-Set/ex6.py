# issubset()	Returns whether another set contains this set or not
# both sets are same it will returns ture

# both sets are difference it will returns False
print({1,2,3,4,5,6}.issubset({11,22,33,44,55}))
# False

print({11,22,33,44,55}.issubset({11,22,33,44,55,1}))
# True

