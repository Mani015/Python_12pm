# count()	Returns the number of elements with the specified value

l4  = ['realme','vivo','oopo','iphone','samsung','redme','micromax','lava','nokia']

print(l4)
# ['realme', 'vivo', 'oopo', 'iphone', 'samsung', 'redme', 'micromax', 'lava', 'nokia']
# sy: listname.count(value)

# l4.count()
# print(l4)
# TypeError: list.count() takes exactly one argument (0 given)


print(l4.count('vivo'))
# 1
print(l4.count('realme'))
# 1

l = [1,2,3,4,5,6,7,1,2,3,4,5,True]
print(l.count(1))
# 3

print('applebananamango'.count('a'))
# 5

