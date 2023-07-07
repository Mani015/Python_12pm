
l1 = [1,2,3,4,5,6,7,8,9,10]

l2 = [11,22,33,44,55,66,77,88,99]
# with out given any data type
# print(zip(l1,l2))
# <zip object at 0x0000022792624940>

# print(list(zip(l1,l2)))
# [(1, 11), (2, 22), (3, 33), (4, 44), (5, 55), (6, 66), (7, 77), (8, 88), (9, 99)]



stu = ['Telugu','hindi','English','Maths','Science','Social']
marks = [98,99,89,95,90,100]

Progress = {}
for key ,value in zip(stu,marks):
    Progress[key] = value
print(Progress)

#
# {'Telugu': 98, 'hindi': 99, 'English': 89, 'Maths': 95, 'Science': 90, 'Social': 100}


