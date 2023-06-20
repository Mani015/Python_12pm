# Nested List:
#  A list inside another list is callled nested list

x1 = [1,2,3,4,5,6,[1,2,3,4,5,6],7,8,9,0]
# print(x1[0])
# 1
# print(x1[1])
# 2
# print(x1[3])
# 4
# print(x1[4])
# 5
# print(x1[5])
# 6
# print(x1[6])
#[1, 2, 3, 4, 5, 6]
# print(x1[7])
# 7

# slicing:
print(x1[1:])
# [2, 3, 4, 5, 6, [1, 2, 3, 4, 5, 6], 7, 8, 9, 0]
print(x1[:6])
# [1, 2, 3, 4, 5, 6]
print(x1[:7])
# [1, 2, 3, 4, 5, 6, [1, 2, 3, 4, 5, 6]]


x1 = [1,2,3,4,5,6,[1,2,3,4,5,6],7,8,9,0]
print(x1[1:7])
# [2, 3, 4, 5, 6, [1, 2, 3, 4, 5, 6]]

print(x1[6][0])
# 1
print(x1[6][-1])
# 6
print(x1[6][5])
# 6



