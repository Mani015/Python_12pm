# if tou want add one value in existing list


l2 = [1,2,3,4,5,6,7,8,9]
print('before list:',l2)
# before list: [1, 2, 3, 4, 5, 6, 7, 8, 9]
# adding the 10

# we are using append method()
# sysntax: listname.append(value)

# append()	Adds an element at the end of the list

l2.append(10)
print('after list:',l2)
# after list: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

l2.append('Apple')
print(l2)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Apple']


l2.append('mango')
print(l2)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Apple', 'mango']

# will adding two vales
l2.append(12.0,13+5j)
print(l2)
# TypeError: list.append() takes exactly one argument (2 given)
