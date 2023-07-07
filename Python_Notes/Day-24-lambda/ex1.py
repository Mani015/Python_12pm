

x = [1,2,3,4,5,6,7,8]

# for i in x:
#     if i>5:
#         print(i)
    # 6
    # 7
    # 8

#
# for i in x:
#     if i>5:
#         print(list(i))
# TypeError: 'int' object is not iterable


# To stored in a list
l1 = []
for i in x:
    if i>5:
        l1.append(i)
print(l1)

# [6, 7, 8]
