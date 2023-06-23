x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}

# both sets are same it will return True (at least one elemenpresent the another set it will return true)
z = x.issuperset(y)
print(z)
# True

# both sets are difference it will return False
print({1,2,3,4,5,6,7}.issuperset({11,22,33,44,55}))
# False