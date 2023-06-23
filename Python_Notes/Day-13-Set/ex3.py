
# discard()	Remove the specified item,

# syntax: set.discard(value)

s2 = {'apple','banana','lemon','orange','watermelon','mango'}

s2.discard('lemon')
print(s2)
# {'mango', 'apple', 'banana', 'orange', 'watermelon'}

s2.discard('mango')
print(s2)
# {'watermelon', 'banana', 'orange', 'apple'}

s2.remove('apple')
print(s2)
# {'orange', 'banana', 'watermelon'}

# s2.remove('papaya')
# print(s2)
# KeyError: 'papaya'
print()
s2.discard('papaya')
print(s2)
# {'watermelon', 'banana', 'orange'}
