
# difference_update()	Removes the items in this set that are also included in another, specified set


x1 = {'shiva','ramu','dinesh','vinod','bhaskar'}
x2 = {'vishal','dhamu','jakir','vinod'}

# print(x1.difference(x2))
# {'dinesh', 'shiva', 'bhaskar', 'ramu'}

# print('before x1 set:',x1)
# before x1 set: {'vinod', 'dinesh', 'shiva', 'ramu', 'bhaskar'}
# difference_update is update before . set
# x1.difference_update(x2)
# x1-x2=x
# print('after updating x1 set:',x1)

# after updating x1 set: {'dinesh', 'shiva', 'ramu', 'bhaskar'}


s1  = {1,2,3,4,5,6,7,11,22,33,44}
s2 = {1,2,3,4,5,6,7,55,66}

print('before update set s2:',s2)
# before update set s2: {1, 2, 3, 4, 5, 6, 7, 66, 55}
s2.difference_update(s1)

print('after updated set s2:',s2)
# after updated set s2: {66, 55}
