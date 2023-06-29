

# for k in range(1,100):
#     if k%2==0:
#         print(k,end=' ')
# 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 42 44 46 48 50 52 54 56 58 60 62 64 66 68 70 72 74 76 78 80 82 84 86 88 90 92 94 96 98



x1 = [0,1,2,3,4,5,6,7,8,9,10]
# for i in x1:
#     print(list(i+1))
# TypeError: 'int' object is not iterable

x2 = []
for i in x1:
    x2.append(i+1)
print(x2)
# output: [2,3,4,5,6,7,8,9,10,11]

# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
