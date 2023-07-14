# In the given list negitve values are converted into a zero like ' 0 '
x1 = [1,2,3,-5,3,-6,-4,-6,-7,-2,11,23]
#
# l1 = []
# for x in x1:
#     if x<0:
#         print(0)
#         l1.append(0)
#     else :
#         print(x)
#         l1.append(x)
# print(l1)



for i in range(len(x1)):
    if x1[i]<0:
        x1[i]=0
print(x1)
# [1, 2, 3, 0, 3, 0, 0, 0, 0, 0, 11, 23]


# summer is very hot

