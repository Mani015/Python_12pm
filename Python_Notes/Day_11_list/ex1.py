# pop()	Removes the element at the specified position

x1 = [1,2,3,4,5,6,7,8,9,10]
print(x1)
# sy: list.pop(index position)
x1.pop(1)
print(x1)
# [1, 3, 4, 5, 6, 7, 8, 9, 10]
x1.pop(5)
print(x1)
# [1, 3, 4, 5, 6, 8, 9, 10]


# I ll give without indexing value

# i didn't passing any index value by default remove end of the value from current list
x1.pop()
print(x1)
# [1, 3, 4, 5, 6, 8, 9]


x2 = ['one','two','three','four','five']
x2.pop()
print(x2)
# ['one', 'two', 'three', 'four']
x2.pop()
print(x2)
# ['one', 'two', 'three']
x2.pop()
print(x2)
# ['one', 'two']


x2.pop(2)
print(x2)
# IndexError: pop index out of range
