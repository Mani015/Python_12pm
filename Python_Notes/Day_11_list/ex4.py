

l1 = [1,2,3,4,5,6,7,8,9,10]
print(l1)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l1[0]='Shiva'
print(l1)
# ['Shiva', 2, 3, 4, 5, 6, 7, 8, 9, 10]
l1[1] = 'Sridhar'
print(l1)
# ['Shiva', 'Sridhar', 3, 4, 5, 6, 7, 8, 9, 10]

# we are using insert method()
# insert()	Adds an element at the specified position
# syntax: list.inser(index,value)
l1.insert(3,'saikiran')
print(l1)
# ['Shiva', 'Sridhar', 3, 'saikiran', 4, 5, 6, 7, 8, 9, 10]

l1.insert(5,'Vishal')
print(l1)
# ['Shiva', 'Sridhar', 3, 'saikiran', 4, 'Vishal', 5, 6, 7, 8, 9, 10]

l1.insert(7,'jakir')
print(l1)
# ['Shiva', 'Sridhar', 3, 'saikiran', 4, 'Vishal', 5, 'jakir', 6, 7, 8, 9, 10]

